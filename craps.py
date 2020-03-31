import random
import time
#Funcoes de aposta
def pass_line(dados,aposta):
    if dados in {7,11}:
        return ("ganhou", 2*aposta)
    if dados in {2,3,12}:
        return ("perdeu", aposta)
    return ("point", aposta)

def field(dados,aposta):
    if dados in {5,6,7,8}:
        return ("perdeu", aposta)
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
apostas = {"pass line":pass_line,"field":field,"any craps":any_craps,"twelve":twelve}
apostas_disponiveis = []
funcoes = globals().copy()
funcoes.update(locals())

while continua_jogando:
    continua_jogando = quer_continuar(fichas,fases[fase])
    dados = random.randint(1,6) + random.randint(1,6)

    continuar = True
    apostas_escolhidas = []
    valores_apostados = []
    apostas_disponiveis = list(apostas.keys())
    while continuar:
        print("você tem {} fichase fez {} apostas. Quer adicionar uma aposta?".format(fichas,len(apostas_escolhidas)))
        for i,item in enumerate(apostas_disponiveis):
            print("{}. {}".format(i+1,apostas_disponiveis[i]))
        try:
            resposta = int(input("{}. finalizar apostas \n".format(len(apostas_disponiveis)+1)))
        except:
            resposta = 6
        if not resposta in range(1,len(apostas_disponiveis)+2):
            print("resposta invalida\n \n")
            time.sleep(1)
        elif resposta == len(apostas_disponiveis)+1:
            continuar = False
        else:
            apostas_escolhidas.append(apostas[apostas_disponiveis[resposta-1]])
            valores_apostados.append(int(input("quanto quer apostar?")))
            del apostas_disponiveis[resposta-1]
            
        
    print("\n a soma dos dados deu: {}".format(dados))

    for i,aposta in enumerate(apostas_escolhidas):
        nome = list(apostas.keys())[list(apostas.values()).index(aposta)]
        resultado = aposta(dados,valores_apostados[i])
        if resultado[0] ==  "ganhou":
            fichas += resultado[1]
            print("voce ganhou {} fichas na aposta {}".format(resultado[1]-valores_apostados[i],nome))
        elif resultado[0] == "perdeu":
            print("voce perdeu a aposta {}".format(nome))
        
