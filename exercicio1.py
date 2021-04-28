'''Exercício de fixação1. Escreva um script python para ler
 uma sequencia de linhas de um arquivo e criar dois outros 
 arquivos separando os número pares e números impares.'''
import os
from os import path
import random

/

with open(path.join(base_dir, "data.txt"), "w") as file:
    for i in range(10):
        num = random.randint(1, 1000)
        file.write(f"{num}\n")

with open(path.join(base_dir, "data.txt")) as file:
    linhas = file.readlines()
    for linha in linhas:
        if int(linha) % 2 == 0:
            with open(path.join(base_dir, "pares.txt"), "a") as par:
                par.write(f"{linha}")
                print(f"{linha.strip()} é par")

        else:
            with open(path.join(base_dir, "impares.txt"), "a") as impar:
                impar.write(f"{linha}")
                print(f"{linha.strip()} é ímpar")



