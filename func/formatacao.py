def formatar_brl(valor):
    """
    Formata um valor em BRL com pontos como separadores de milhar e vírgula para decimais.
    Exemplo: 9505072.00 -> "9.505.072,00"
    """
    parte_inteira, parte_decimal = f"{valor:.2f}".split('.')
    parte_inteira_formatada = ""
    for i, char in enumerate(reversed(parte_inteira), 1):
        parte_inteira_formatada = char + parte_inteira_formatada
        if i % 3 == 0 and i != len(parte_inteira):
            parte_inteira_formatada = '.' + parte_inteira_formatada
    return f"{parte_inteira_formatada},{parte_decimal}"