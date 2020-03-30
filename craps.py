#Funcoes de aposta
def pass_line(dados,aposta):
    if dados in {7,11}:
        return ("ganhou", 2*aposta)
    if dados in {2,3,12}:
        return ("perdeu", 0)
    return ("point", aposta)

def field(dados,aposta):
    if dados in {5,6,7,8}:
        return ("perdeu", 0)
    if dados in {3,4,9,10,11}:
        return ("ganhou", 2*aposta)
    if dados == 2:
        return ("ganhou", 3*aposta)
    return ("ganhou", 4*aposta)

def any_craps(dados,aposta):
    if dados in {2,3,12}:
        return ("ganhou", 8*aposta)
    return ("perdeu", 0)

def twelve(dados,aposta):
    if dados == 12:
        return ("ganhou", 31*aposta)
    return ("perdeu", 0)

def quer_continuar(fichas,fase):
    while True:
        jogar = input("você tem {} fichas e esta na fase {}. Quer conttinuar jogando?(s/n)".format(fichas,fase))
        if jogar == "s":
            return True
        elif jogar == "n":
            return False
        print("resposta invalida")

continua_jogando = True
fichas = 100
fases = ["come out","point"]
fase = 0
apostas = [pass_line,field,any_craps,twelve]
apostas_disponiveis = []

while continua_jogando:
    continua_jogando = quer_continuar(fichas,fases[fase])
