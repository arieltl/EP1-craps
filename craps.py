def pass_line(dados,aposta):
    if dados in [7,11]:
        return "ganhou", 2*aposta
    if dados in [2,3,12]:
        return "perdeu", 0
    return "point", aposta