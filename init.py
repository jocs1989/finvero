from config.settings import *
from db.psql import PostgresConnection
from tools.seed import seed
from scraper.alibaba import Alibaba
# Uso del Singleton para conectarse a PostgreSQL
import argparse
#url = "https://www.alibaba.com/showroom/power-banks-%2526-power-station/ultra-slim/p100010895.html?spm=a2700.7724857.0.0.27811c8cdbcfEf"
#url = "https://www.alibaba.com/showroom/power-banks-%2526-power-station/waterproof/p100010895.html?spm=a2700.7724857.0.0.27811c8cPEuTe0"
#url = "https://www.aequired=Falselibaba.com/showroom/power-banks-%2526-power-station/large-capacity/p100010895.html?spm=a2700.7724857.0.0.331a2a47TeY4nw"
#url = "https://www.alibaba.com/showroom/handbags/unisex/p100002856.html?spm=a2700.7724857.0.0.2ff72a97o6ytdr"
#url = "https://www.alibaba.com/showroom/handbags/women/p100002856.html?spm=a2700.7724857.0.0.25607fdaRev4cE"

url = "https://www.alibaba.com/showroom/ali-baba.html?gad_source=1&gclid=EAIaIQobChMI2LnDqMnJhQMVmUp_AB29qA_pEAAYASABEgJEgvD_BwE"

def make(url: str):
    if url:
        Alibaba(url).start()
    # Aquí puedes realizar otras operaciones utilizando la semilla


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para el sitio de Alibaba")
    parser.add_argument("--url", type=str, help="URL del sitio web", nargs="?")
    parser.add_argument("--comando", choices=["seed"], help="Ejecuta la creación de tabla", nargs="?")  # Hacer el argumento opcional con nargs="?"
    args = parser.parse_args()

    if args.url is not None:
        make(args.url)

    if args.comando == "seed":
        seed()

    

    
