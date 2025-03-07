import logging
import time
from selenium.webdriver.common.by import By

def verificar_e_contratar_plano(driver, saldo_btc):
    """
    Verifica o valor de BTC/Min, BTC/Day e o tipo de plano.
    Contrata um novo plano se as condições forem atendidas.
    """
    try:
        btc_min_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/section/div/div/div[2]/div/div/div/p[2]/a')
        btc_min = float(btc_min_element.text)

        btc_day_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/section/div/div/div[3]/div/div/div/p[2]/a')
        btc_day = float(btc_day_element.text)

        plano_element = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[2]/section/div/div/div[1]/div/div/div/p[2]/a')
        plano = plano_element.text

        logging.info(f"Plano: {plano} | BTC/Min: {btc_min:.8f} | BTC/Day: {btc_day:.8f}")

        if btc_min == 0.00000050 and saldo_btc >= 0.005:
            logging.info("Condições atendidas para contratar o próximo plano: BTC/Min = 0.00000200, BTC/Day = 0.00288")
            botao_contratar = driver.find_element(By.XPATH, '//*[@id="pricing_upgrade"]/div/div/div/div/div/div/div/div/u/div[2]/a')
            botao_contratar.click()
            logging.info("Novo plano contratado com sucesso!")
            time.sleep(5)

        elif btc_min == 0.00000200 and saldo_btc >= 0.009:
            logging.info("Condições atendidas para contratar o próximo plano: BTC/Min = 0.00000400, BTC/Day = 0.00576")
            botao_contratar = driver.find_element(By.XPATH, '//*[@id="pricing_upgrade"]/div/div/div/div/div/div/div/div/u/div[2]/a')
            botao_contratar.click()
            logging.info("Novo plano contratado com sucesso!")
            time.sleep(5)

        elif btc_min == 0.00000400 and saldo_btc >= 0.02:
            logging.info("Condições atendidas para contratar o próximo plano: BTC/Min = 0.00001200, BTC/Day = 0.01728")
            botao_contratar = driver.find_element(By.XPATH, '//*[@id="pricing_upgrade"]/div/div/div/div/div/div/div/div/u/div[2]/a')
            botao_contratar.click()
            logging.info("Novo plano contratado com sucesso!")
            time.sleep(5)

        elif btc_min == 0.00001200 and saldo_btc >= 0.09:
            logging.info("Condições atendidas para contratar o próximo plano: BTC/Min = 0.00004800, BTC/Day = 0.06912")
            botao_contratar = driver.find_element(By.XPATH, '//*[@id="pricing_upgrade"]/div/div/div/div/div/div/div/div/u/div[2]/a')
            botao_contratar.click()
            logging.info("Novo plano contratado com sucesso!")
            time.sleep(5)

    except Exception as e:
        logging.error(f"Erro ao verificar/contratar plano: {e}")