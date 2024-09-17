import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Ejercicio 1
busqueda = 'cerveza turia'
web = requests.get('https://tienda.consum.es/es/s/' + busqueda.replace(" ", "%20"))
soup = BeautifulSoup(web.text, "lxml")
articulos = soup.find_all('div', {'class': 'product-tile'})
for articulo in articulos:
    print(articulo.text.strip())  # Imprime el texto del artículo

# Ejercicio 2
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver', options=options)
busqueda = 'cerveza turia'
wd.get("https://www.carrefour.es/?q=" + busqueda.replace(" ", "+"))
soup = BeautifulSoup(wd.page_source, "lxml")
articulos = soup.find_all('div', {'class': 'cl-product-tile__description'})
for articulo in articulos:
    print(articulo.text.strip())  # Imprime el texto del artículo#

# Ejercicio 3
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# Aquí es donde cargarías tus datos, ya sea a través de webscraping u otras técnicas
carrefour_productos = {'Chocolate con leche Milka 270 g.': '2,10 €',
                       'Galletas con chocolate Choco Biscuits Milka 150 g.': '1,91 €'}
consum_productos = {'Chocolate con Leche 270 Gr': '1,85 €', 'Chocolate Triple 90 Gr': '1,29 €'}

productos = []
for producto_c, precio_c in carrefour_productos.items():
    for producto_con, precio_con in consum_productos.items():
        similitud = similar(producto_c, producto_con)
        if similitud > 0.66:
            productos.append(
                {'consum': {producto_con: precio_con}, 'carrefour': {producto_c: precio_c}, 'similarity': similitud})

print(productos)