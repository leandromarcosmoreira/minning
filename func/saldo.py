import logging
from selenium.webdriver.common.by import By
from func.formatacao import formatar_brl

def verificar_saldo(driver, cotacao_btc_brl=None):
    """
    Verifica o saldo atual na página e exibe o valor em BTC e BRL.
    Retorna o saldo em BTC.
    """
    saldo_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[1]/section/div/div[1]/div/h1')
    saldo_texto = saldo_element.text
    try:
        saldo_btc = float(saldo_texto)
        saldo_brl = saldo_btc * cotacao_btc_brl if cotacao_btc_brl else None
        logging.info(f"Saldo atual: {saldo_btc:.8f} BTC" + (f" | R$ {formatar_brl(saldo_brl)} BRL" if saldo_brl else ""))
        
        return saldo_btc
    except ValueError:
        logging.error(f"Erro ao converter saldo: '{saldo_texto}' não é um número válido.")
        return 0.0