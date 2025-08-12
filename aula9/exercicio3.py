""""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas=[] 
soma= media =0

for i in range (4):
    nota= float (input(f'digite a {i+1}º nota=>'))
    notas.append(nota)
    soma+= nota
media= soma/4
for i in range (4):
    print(f'{i+1}º nota foi {notas[i]}')
print(f'a media foi:{media}')
