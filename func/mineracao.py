import time
import logging
from selenium.webdriver.common.by import By

def iniciar_mineracao(driver, btc_address):
    """
    Inicia o processo de mineração para um carteira de Bitcoin.
    """
    driver.get("https://www.freemining.club/")
    msg = f"Processando carteira: {btc_address}"
    logging.info(f"{'-' * len(msg)}")
    logging.info(f"{msg}")
    logging.info(f"{'-' * len(msg)}")
    time.sleep(5)
    
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div/div[1]/div[1]/div/div/button").click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="addr2"]').send_keys(btc_address)
    
    driver.find_element(By.XPATH, '//*[@id="add_formid"]/div/div[2]/div/div/button').click()
    time.sleep(5)