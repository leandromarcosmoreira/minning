from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def configurar_navegador():
    """
    Configura e retorna uma instância do navegador Chrome em modo headless.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=chrome_options)