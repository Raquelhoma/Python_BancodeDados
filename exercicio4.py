'''4.Escreva um script que LEIA os dados do arquivo 
texto gerado na questão anterior e exiba no console 
apenas os nomes dos alunos concatenado com a frase 
a seguir, baseado em sua regra: 
I.“em fase de adaptação” (escore menor do que 6), 
II.“familiarizado com o curso” (escore entre 6.0 e 7.0 –intervalo fechado), 
III.“em excelência no curso” (escore maior que 7,0 e menor que 8.5)
IV.“Nasceu para o curso” (escore acima de 8.5).'''

import os
from os import path

base_dir = path.dirname(path.abspath(__file__))

with open(path.join(base_dir, 'usuarios3.txt')) as file:
    usuarios = file.readlines()
    for usuario in usuarios:
        dados = usuario.split(";")
        score = float(dados[3])

        if score < 6:
            print(f'O aluno {dados[1]} está em fase de adaptação')
        elif score >= 6 and score  <= 7:
            print(f'O aluno {dados[1]} está familiarizado com o curso')
        elif score > 7 and score  <= 8.5:
            print(f'O aluno {dados[1]} está em excelência no curso')
        else:
            print(f'o aluno {dados[1]} nasceu para o curso')



    
        
            




    

