"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vetor =[]
total= 0
for i in range(10):
    letra=input(f'digite o {i+1}º caracteres').lower
    vetor.append(letra)
if letra.isalpha() and letra not in 'aeiou':
    total +=1
    print (f' letra  {vetor[i]}')
print(f'foi informado{total} consoantes')