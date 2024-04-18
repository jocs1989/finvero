# Prueba Tecnica:
 
**Objetivo**: Desarrollar un scraper sencillo que extraiga información específica de un sitio web público de elección, como títulos de noticias, precios de productos, o entradas de blog.
Requisitos:
- Utilizar Python para el desarrollo del scraper.
- Extraer al menos tres tipos diferentes de datos del sitio elegido.
- Almacenar los datos extraídos en una base de datos de elección (SQL o NoSQL).
- (Opcional) Utilizar solicitudes asíncronas para mejorar la eficiencia de la extracción.
- Documentar brevemente el código y el proceso de desarrollo, incluyendo cómo se extrajeron los datos y cualquier dificultad enfrentada.
Entregables:
- Código fuente del scraper.
- Scripts de base de datos utilizados para almacenar los datos extraídos.
- Documentación básica del proyecto.

Dejo las variables de entorno no  de ejmplo 

Inicia los contenedores

```bash
docker compose --env-file .env.dev up -d 
```
# Activa el modo de desarollo
```bash
python3 -m venv .env

source .env/bin/activate 
```
Crea la base datos 
```bash
python3 init.py seed  


```
Crea el escraper
```bash
 python3 init.py --url https://www.alibaba.com/showroom/power-banks-%2526-power-station/ultra-slim/p100010895.html\?spm\=a2700.7724857.0.0.27811c8cdbcfEf 


```
