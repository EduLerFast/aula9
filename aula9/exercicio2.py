"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = []

for i in range(10):
    l = float (input(f'Digite o {i+1}¹ numero da lista'))

    lista.append(l)
#mostre na ordem inversa.

lista.reverse ()
for i in range(10):
    print(f'posiçao -> {i} na lista, tem o conteudo {lista[i]}')