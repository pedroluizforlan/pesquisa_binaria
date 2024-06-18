import math

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def pesquisa_binaria(lista, numero):
    posicao_mais_baixa = 0
    posicao_mais_alta = len(lista) - 1

    while posicao_mais_baixa <= posicao_mais_alta:
        posicao_meio = (posicao_mais_baixa + posicao_mais_alta) / 2
        posicao_meio = math.ceil(posicao_meio)
        chute_atual = lista[posicao_meio]
        if chute_atual == numero:
           return print("Você encontrou o numero")
        if(chute_atual > numero):
            posicao_mais_alta = posicao_meio - 1
            print("o chute é mais bixo")
        else:
            posicao_mais_baixa = posicao_meio + 1
            print("o chute é mais alto")   
    return None


pesquisa_binaria(arr,3)