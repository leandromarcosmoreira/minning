import logging
import time
from selenium.webdriver.common.by import By

def processar_saque(driver):
    """
    Processa o saque se o saldo for suficiente.
    """
    valor_total_element = driver.find_element(By.XPATH, '//*[@id="widthsum"]')
    valor_total = valor_total_element.get_attribute("value")
    logging.info(f"Valor total disponível para saque: {valor_total} BTC")
    driver.find_element(By.XPATH, '//*[@id="btnwithdraw1"]').click()
    logging.info("Botão 'CONFIRM' clicado!")
    time.sleep(3)