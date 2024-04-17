from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://portfolio2-0-iota-nine.vercel.app'
driver.get(url)

# Encontrar o título da página
titulo = driver.find_element(By.XPATH, "//title")
titulotexto = titulo.get_attribute("innerText")

# Encontrar a div com a classe "aboutme"
about_me_div = driver.find_element(By.CLASS_NAME, "aboutme")

# Obter o texto da div
about_me_text = about_me_div.get_attribute('innerText')

# Obter as propriedades CSS da div
about_me_css_properties = {}
for prop in ['display', 'font-size', 'margin-block-start', 'margin-block-end', 'margin-inline-start', 'margin-inline-end', 'font-weight']:
    about_me_css_properties[prop] = about_me_div.value_of_css_property(prop)

# Obter as propriedades CSS do elemento body
bodycss = driver.execute_script("""
    var cssProperties = {};
    var cs = window.getComputedStyle(document.body);
    cssProperties['display'] = cs.getPropertyValue('display');
    cssProperties['margin'] = cs.getPropertyValue('margin');
    return cssProperties;
""")

# Obter as propriedades CSS do elemento html
htmlcss = driver.execute_script("""
    var cssProperties = {};
    var cs = window.getComputedStyle(document.documentElement);
    cssProperties['display'] = cs.getPropertyValue('display');
    return cssProperties;
""")

# Imprimir os resultados
print("Titulo da Pagina: ")
print("     ", titulotexto)

print("\nTexto da div 'aboutme':")
print("     ", about_me_text)

print("\nPropriedades especificas da div 'aboutme':")
print("CSS: ")
for prop, value in about_me_css_properties.items():
    print(f"    {prop}: {value}")

print("\nPropriedades especificas do elemento body:")
print("CSS: ")
for prop, value in bodycss.items():
    print(f"    {prop}: {value}")

print("\nPropriedades especificas do elemento html:")
print("CSS: ")
for prop, value in htmlcss.items():
    print(f"    {prop}: {value}")

driver.quit()
