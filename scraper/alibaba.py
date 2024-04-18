import asyncio
from random import uniform
from playwright.async_api import async_playwright
from fake_useragent import UserAgent
from tools.create import insert_db


class Alibaba:
    def __init__(self, url="https://www.alibaba.com/showroom") -> None:
        """
        Inicializa una instancia de la clase Alibaba.

        Args:
            url (str): La URL base para la búsqueda de productos en Alibaba. Por defecto es "https://www.alibaba.com/showroom".
        """
        self.url = url

    async def scrape_website(self):
        """
        Realiza el scraping del sitio web Alibaba para obtener información de productos.
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # Generar un agente de usuario aleatorio
            user_agent = UserAgent().random
            await page.set_extra_http_headers({"User-Agent": user_agent})

            await page.goto(self.url)

            # Esperar a que la página se cargue completamente
            await page.wait_for_load_state("networkidle")

            # Esperar un tiempo aleatorio para simular el comportamiento humano
            await asyncio.sleep(uniform(2, 5))

            # Emular el desplazamiento de la página si es necesario
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

            # Esperar un tiempo aleatorio para simular el comportamiento humano
            await asyncio.sleep(uniform(2, 7))

            # Obtener los enlaces de la página usando una clase específica
            # Seleccionar el elemento padre
            elemento_padre = await page.query_selector(".component-product-list")

            if elemento_padre:
                # Buscar el elemento con la clase 'product-card-gallery' dentro del elemento padre
                elementos_hijos = await elemento_padre.query_selector_all(
                    ".product-card-gallery.product-card"
                )

                for elemento_hijo in elementos_hijos:
                    # Extraer la URL del producto
                    url_elemento = await elemento_hijo.query_selector(
                        "div.image-switcher a.product-image"
                    )
                    url_producto = await page.evaluate(
                        '(element) => element.getAttribute("href")', url_elemento
                    )

                    # Extraer la imagen
                    imagen_elemento = await elemento_hijo.query_selector(
                        ".product-image img"
                    )
                    imagen_src = await page.evaluate(
                        '(element) => element.getAttribute("src")', imagen_elemento
                    )

                    # Extraer el texto
                    texto_elemento = await elemento_hijo.query_selector("h2 a")
                    texto = await page.evaluate(
                        "(element) => element.textContent", texto_elemento
                    )

                    # Extraer el precio
                    precio_elemento = await elemento_hijo.query_selector(
                        ".product-price .price-number"
                    )
                    precio = await page.evaluate(
                        "(element) => element.textContent", precio_elemento
                    )

                    # Extraer la cantidad
                    cantidad_elemento = await elemento_hijo.query_selector(
                        ".product-moq-number"
                    )
                    cantidad = await page.evaluate(
                        "(element) => element.textContent", cantidad_elemento
                    )

                    # Imprimir la información extraída
                    insert_db((url_producto,
                               imagen_src,
                               texto,
                               precio,
                               cantidad))

            else:
                print("El elemento padre no fue encontrado")

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.scrape_website())

        



