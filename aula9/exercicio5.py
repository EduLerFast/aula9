"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
vetor=[]
vetorpar=[]
vetorimpar=[]
for i in range (20):
    n= int (input(f'digite o {i+1}º numero=>'))
    vetor.append(n)

    if n % 2==0:
        vetorpar.append(n)
    else:
        vetorimpar.append(n)
print(f'vetor {vetor}')
print(f'vetor {vetorpar}')
print(f'vetor {vetorimpar}')