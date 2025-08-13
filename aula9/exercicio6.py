"""
6=Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
aluno1=[]
aluno2=[]
aluno3=[]
aluno4=[]
aluno5=[]
aluno6=[]
aluno7=[]
aluno8=[]
aluno9=[]
aluno10=[]
quant=0
for i in range(10):
    print(f"aluno {i+1}")
    for j in range(4):
        nota= float (input(f'coloque a {j+1}ª nota'))
        if i==0:
            aluno1 .append(nota)
        elif i==1:
            aluno2 .append(nota)
        elif i==2:
            aluno3 .append(nota)
        elif i==3:
            aluno4 .append(nota)
        elif i==4:
            aluno5 .append(nota)
        elif i==5:
            aluno6 .append(nota)
        elif i==6:
            aluno7 .append(nota)
        elif i==7:
            aluno8 .append(nota)
        elif i==8:
            aluno9 .append(nota)
        elif i==9:
            aluno10 .append(nota)

if ((aluno1[0] + aluno1[1]+aluno1[2] + aluno1[3])/4)>=7:
    print('O aluno 1 tem a media maior que 7')
    quant+=1
if ((aluno2[0] + aluno2[1]+aluno2[2] + aluno2[3])/4)>=7:
    print('O aluno 2 tem a media maior que 7')
    quant+=1
if ((aluno3[0] + aluno3[1]+aluno3[2] + aluno3[3])/4)>=7:
    print('O aluno 3 tem a media maior que 7')
    quant+=1
if ((aluno4[0] + aluno4[1]+aluno4[2] + aluno4[3])/4)>=7:
    print('O aluno 4 tem a media maior que 7')
    quant+=1
if ((aluno5[0] + aluno5[1]+aluno5[2] + aluno5[3])/4)>=7:
    print('O aluno 5 tem a media maior que 7')
    quant+=1
if ((aluno6[0] + aluno6[1]+aluno6[2] + aluno6[3])/4)>=7:
    print('O aluno 6 tem a media maior que 7')
    quant+=1
if ((aluno7[0] + aluno7[1]+aluno7[2] + aluno7[3])/4)>=7:
    print('O aluno 7 tem a media maior que 7')
    quant+=1
if ((aluno8[0] + aluno8[1]+aluno8[2] + aluno8[3])/4)>=7:
    print('O aluno 8 tem a media maior que 7')
    quant+=1
if ((aluno9[0] + aluno9[1]+aluno9[2] + aluno9[3])/4)>=7:
    print('O aluno 9 tem a media maior que 7')
    quant+=1
if ((aluno10[0] + aluno10[1]+aluno10[2] + aluno10[3])/4)>=7:
    print('O aluno 10 tem a media maior que 7')
    quant+=1

print (f'{quant} alunos tem a media igual ou maior que 7')