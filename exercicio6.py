'''6. Escreva uma função que recebe dois nomes 
de arquivos e copia o conteúdo do primeiro arquivo 
para o segundo arquivo. Considere que o conteúdo do 
arquivo de origem é um texto. Sua função não deve 
copiar linhas comentadas (que começam com //).'''

import os
from os import path

base_dir = path.dirname(path.abspath(__file__))

def copiarArquivo(arquivo3):
    with open(path.join(base_dir, 'arq6_2.txt'), 'a') as file:
        file.write(f'{arquivo3}\n')
            


with open(path.join(base_dir, 'arq6_1.txt'), 'r') as file:
    arquivo1 = file.readlines()    
    for linha in arquivo1:
        linhas_sem_branco = linha.strip()        
        if "//" not in linhas_sem_branco:
            arquivo2 = linhas_sem_branco
            copiarArquivo(arquivo2)


            


      
  
    
            


    

        
        



