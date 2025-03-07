import requests
import logging

def obter_cotacao_btc_para_brl():
    """
    Obtém a cotação atual do Bitcoin em Reais (BRL) usando a API do CoinGecko.
    Retorna o valor da cotação ou None em caso de erro.
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados["bitcoin"]["brl"]
    except Exception as e:
        logging.error(f"Erro ao obter cotação do Bitcoin: {e}")
        return None