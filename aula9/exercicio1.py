"""
1-Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
#CRIAR LISTA
lista = []
#varrer a lista para cinco numeros
for i in range(5):
    l = int (input(f'Digite o {i+1}¹ numero da lista'))
#gravando numero na lista
    lista.append(l)
#imprime o counteudo da lista
for i in range(5):
    print(f'posiçao -> {lista} na lista, tem o conteudo {lista[i]}')