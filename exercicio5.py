'''5. Faça um programa que leia um número N e 
gere um arquivo com N nomes e idades aleatórios. 
Faça uso de duas listas criadas na mão: uma que 
contenha 20 nomes e outra que contenha 20 sobrenomes. 
Cada linha do arquivo resultante deve conter um nome 
completo e a sua idade.'''

import os
from os import path
import random

base_dir = path.dirname(path.abspath(__file__))

nomes = ['Ana', 'Paula', 'Pedro', 'Jose', 'Maria', 'Andre', 'Antonio', 'Mario', 'Vivi', 'Caco']
sobrenomes = ['Veronese', 'Picollo', 'Pucci', 'Simoni', 'Boschetti', 'Mellone', 'Paiano', 'Bocceli', 'Dana', 'Bezerra']

with open(path.join(base_dir, "listanomes.txt"), "w") as file:
    for i in range(9):
        idade = random.randint(0, 120)
        indice_nome = random.randint(0, len(nomes)-1)
        indice_sobrenome = random.randint(0,len(sobrenomes)-1)

        file.write(f'{nomes[indice_nome]} {sobrenomes[indice_sobrenome]} com {idade} anos\n')
      




    
 