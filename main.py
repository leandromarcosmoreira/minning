import logging
from func.cotacao import obter_cotacao_btc_para_brl
from func.navegador import configurar_navegador
from func.mineracao import iniciar_mineracao
from func.saldo import verificar_saldo
from func.plano import verificar_e_contratar_plano
from func.sumario import formatar_sumario
from func.formatacao import formatar_brl

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("execution.log"),
        logging.StreamHandler()
    ]
)

def ler_carteiras_do_arquivo(caminho_arquivo):
    """
    Lê as carteiras de Bitcoin de um arquivo de texto.
    Retorna uma lista de carteiras e o número total de linhas.
    """
    try:
        with open(caminho_arquivo, "r") as arquivo:
            carteiras = [linha.strip() for linha in arquivo if linha.strip()]
        return carteiras, len(carteiras)
    except Exception as e:
        logging.error(f"Erro ao ler o arquivo de carteiras: {e}")
        return [], 0

def main():
    """
    Função principal que executa o script.
    """

    caminho_arquivo_carteiras = "carteiras.txt"
    btc_addresses, total_carteiras = ler_carteiras_do_arquivo(caminho_arquivo_carteiras)

    if not btc_addresses:
        logging.error("Nenhuma carteira foi carregada. Verifique o arquivo 'carteiras.txt'.")
        return

    sumario = []

    cotacao_btc_brl = obter_cotacao_btc_para_brl()
    if cotacao_btc_brl:
        logging.info(f"Cotação atual do Bitcoin: R$ {formatar_brl(cotacao_btc_brl)} BRL")
    else:
        logging.warning("Não foi possível obter a cotação do Bitcoin. Exibindo apenas saldos em BTC.")

    for indice, btc_address in enumerate(btc_addresses, start=1):
        msg=f"Processando carteira {indice}/{total_carteiras}: {btc_address}"
        logging.info(len(msg) * "-")
        logging.info(msg)
        logging.info(len(msg) * "-")
        driver = configurar_navegador()
        try:
            iniciar_mineracao(driver, btc_address)
            saldo_btc = verificar_saldo(driver, cotacao_btc_brl)
            sumario.append((btc_address, saldo_btc))

            verificar_e_contratar_plano(driver, saldo_btc)
            
            if saldo_btc >= 0.1:
                processar_saque(driver)
        
        except Exception as e:
            logging.error(f"Erro com o carteira {btc_address}: {e}")
        
        finally:
            driver.quit()
    
    formatar_sumario(sumario, cotacao_btc_brl)

if __name__ == "__main__":
    main()