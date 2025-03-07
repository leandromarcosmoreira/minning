import logging
from func.formatacao import formatar_brl

def formatar_sumario(sumario, cotacao_btc_brl):
    """
    Formata e exibe o sumário dos saldos em formato de tabela, incluindo o total.
    """
    if not sumario:  # Verifica se a lista sumario está vazia
        logging.warning("Nenhum saldo foi processado. O sumário está vazio.")
        return

    tamanho_endereco = max(len(endereco) for endereco, _ in sumario) + 2
    tamanho_saldo_btc = 15
    tamanho_saldo_brl = 20

    saque_minimo_btc = 0.005
    saque_minimo_brl = saque_minimo_btc * cotacao_btc_brl if cotacao_btc_brl else 0.0
    saque_msg = f"Saque mínimo por carteira: {saque_minimo_btc:.8f} BTC | R$ {formatar_brl(saque_minimo_brl)}"
    separador = "-" * (tamanho_endereco + tamanho_saldo_btc + tamanho_saldo_brl + 9)
    logging.info(len(saque_msg) * "-")
    logging.info(saque_msg)
    logging.info(len(saque_msg) * "-")

    cabecalho = f"{'Carteira':<{tamanho_endereco}} | {'Saldo (BTC)':<{tamanho_saldo_btc}} | {'Saldo (BRL)':<{tamanho_saldo_brl}}"
    logging.info(cabecalho)
    logging.info(separador)

    total_btc = 0.0
    total_brl = 0.0

    for endereco, saldo_btc in sumario:
        saldo_brl = saldo_btc * cotacao_btc_brl if cotacao_btc_brl else 0.0
        linha = f"{endereco:<{tamanho_endereco}} | {saldo_btc:>{tamanho_saldo_btc}.8f} | R$ {formatar_brl(saldo_brl):>{tamanho_saldo_brl}}"
        logging.info(linha)

        total_btc += saldo_btc
        total_brl += saldo_brl

    linha_total = f"{'Total':<{tamanho_endereco}} | {total_btc:>{tamanho_saldo_btc}.8f} | R$ {formatar_brl(total_brl):>{tamanho_saldo_brl}}"
    logging.info(separador)
    logging.info(linha_total)
    logging.info(separador)