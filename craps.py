import random
import time
from enum import Enum

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

def point(dados,valor):
    if dados == valor:
        return("ganhou")
    elif dados == 7:
        return("perdeu")
    return

class Fase(Enum):
    comeout = "Come Out"
    point = "Point"

#variaveis  
fichas = 100

fase = Fase.comeout
apostas = {"pass line":pass_line,"field":field,"any craps":any_craps,"twelve":twelve}
apostas_disponiveis = []
funcoes = globals().copy()
funcoes.update(locals())
#loop de jogo
while fichas >= 0:
    #verifica se jogador quer continuar jogando
    if not quer_continuar(fichas,fase.value):
        break
    
    dados = random.randint(1,6) + random.randint(1,6)

    continuar_a_apostar = True
    apostas_escolhidas = []
    valores_apostados = []
    limite_apostas = 0 if fase == Fase.comeout else 1
    apostas_disponiveis = list(apostas.keys())[limite_apostas:]
    valor_do_point = 0
    valor_apostado_point = 0
    
    #Adicionar apostas na rodada
    while continuar_a_apostar:
        print("você tem {} fichas disponiveis e fez {} apostas. Quer adicionar uma aposta?".format(fichas,len(apostas_escolhidas)))
        #remover aposta pass line se estiver em rodada point
        
        #mostrar apostas disponiveis
        for i,item in enumerate(apostas_disponiveis):
            print("{}. {}".format(i+1,apostas_disponiveis[i]))
        
        #verificar se input é valido
        try:
            resposta = int(input("{}. finalizar apostas \n".format(len(apostas_disponiveis)+1)))
        except:
            resposta = 6
        
        if not resposta in range(1,len(apostas_disponiveis)+2):
            print("resposta invalida\n \n")
            time.sleep(1)
        #finalizar apostas caso o usuario queira
        elif resposta == len(apostas_disponiveis)+1:
            continuar_a_apostar = False
        #contabilziar fichas e adicionar aposta selecionada
        else:
            try:
                aposta = int(input("quanto quer apostar?"))
                if aposta <= fichas:
                    apostas_escolhidas.append(apostas[apostas_disponiveis[resposta-1]])
                    valores_apostados.append(aposta)
                    fichas -= valores_apostados[-1]
                    del apostas_disponiveis[resposta-1]
                else:
                    print("fichas insuficientes")
            except:
                print("resposta invalida")
        
    print("\na soma dos dados deu: {}".format(dados))
    if fase == Fase.point:
            resultado_point = point(dados,valor_do_point)
            if resultado_point == "ganhou":
                fichas += valor_apostado_point 
                print("voce ganhou o point")
                fase = Fase.comeout
            elif resultado_point == "perdeu":
                print("voce perdeu o point")
                fase = Fase.comeout
                
    for i,aposta in enumerate(apostas_escolhidas):
        nome = list(apostas.keys())[list(apostas.values()).index(aposta)]
        resultado = aposta(dados,valores_apostados[i])
        if resultado[0] ==  "ganhou":
            fichas += resultado[1]
            print("voce ganhou {} fichas na aposta {}".format(resultado[1]-valores_apostados[i],nome))
        elif resultado[0] == "perdeu":
            print("voce perdeu a aposta {}".format(nome))
        else:
            print("voce foi para rodada point")
            fase = Fase.point
            valor_apostado_point = resultado[1]
            valor_do_point = dados

    

if fichas <= 0:
    print("Suas fichas acabaram")