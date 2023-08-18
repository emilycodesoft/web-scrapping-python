from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Configuración del navegador
driver = webdriver.Chrome()

# URL de IMDb a la que deseas hacer web scraping
url = "https://www.imdb.com/chart/top"

# Abrir la página en el navegador
driver.get(url)

elements = driver.find_elements(
    By.CLASS_NAME,
    "ipc-metadata-list-summary-item",
)
data = {
    "titulos": [],
    "fecha-publicacion": [],
    "duracion": [],
    "edad-minima": [],
    "puntuacion": [],
}

for item in elements:
    data["titulos"].append(
        item.find_element(By.CLASS_NAME, "ipc-title-link-wrapper")
        .find_element(By.TAG_NAME, "h3")
        .text
    )
    metadata = item.find_element(By.CLASS_NAME, "sc-14dd939d-5").find_elements(
        By.TAG_NAME, "span"
    )
    data["fecha-publicacion"].append(metadata[0].text)
    data["duracion"].append(metadata[1].text)
    data["edad-minima"].append(metadata[2].text)
    data["puntuacion"].append(
        item.find_element(
            By.CLASS_NAME,
            "ipc-rating-star",
        ).text
    )

# Cerrar el navegador
driver.quit()

# print(data)
# Crear un DataFrame de Pandas
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df = pd.DataFrame(data)
df.to_csv("imdb-datos.csv", index=False, sep="=", encoding="utf-8")
