'''3. Escreva um script python que receba do usuário os
seguintes dados de aluno: matrícula, nome, ano de
ingresso, escore atual e grave as informações em um
arquivo texto com os valores de cada aluno em linhas
distintas separados por “;”.'''

import os
from os import path

base_dir = path.dirname(path.abspath(__file__))

with open(path.join(base_dir, 'usuarios3.txt'), 'a') as file:
    opcao = '0'
    while opcao=='0':
        matricula = input('Matrícula: ')
        nome = input('Nome: ')
        ano = input('Ano de ingresso: ')
        escore = input('Escore atual: ')
        file.write(f"{matricula};{nome};{ano};{escore};\n")
        opcao = input('Informe 1 para sair e 0 para continuar: ')

print("**********************************************************")





