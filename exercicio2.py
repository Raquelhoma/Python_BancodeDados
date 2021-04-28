'''2. Escreva um script python para ler todas
 as linhas de um arquivo, ordena-las e 
 salvar novamente no arquivo. '''
 
import os
from os import path
import random

base_dir = path.dirname(path.abspath(__file__))

with open(path.join(base_dir, "arq2.txt"), 'w') as file:
     for i in range(10):
         num = random.randint(1, 50)
         file.write(f"{num}\n")

with open(path.join(base_dir, "arq2.txt")) as file:
    linhas = file.readlines()
    numeros = []
    for linha in linhas:
        numeros.append(int(linha))

    numeros.sort()
    for numero in numeros:
        print(f"{numero}\n")

    






    


