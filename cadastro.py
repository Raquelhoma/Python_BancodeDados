'''2. Escreva funções que realizem respectivamente 
as operações básicas de Create Read Update Delete 
para a tabela de alunos'''
from os import path
from sqlite3 import dbapi2

db_file = path.join(path.dirname(path.abspath(__file__)), 'db_alunos.db')
cx = dbapi2.connect(db_file)

cursor = cx.cursor()

def adicionarAluno():
    nome_aluno = input('Informe o nome do aluno: ')
    data_nascimento = input('Informe a data de nascimento dd/mm/aaaa: ')
    sexo_aluno = (input('Informe o sexo do aluno (M/F): ')).upper()
    cursor.execute('''insert into cadastro_alunos (nome, nascimento, sexo) values (?,?,?)''',
    (nome_aluno, data_nascimento, sexo_aluno))
    cx.commit()

def lerListaAlunos():
    dados_Alunos = cursor.execute('select * from cadastro_alunos;')
    rows = dados_Alunos.fetchall()
    for row in rows:
        print(row)

def atualizarAluno():
    matricula = input('Informe a matricula do aluno para retificar: ')
    novo_nome = input('Informe o novo nome do aluno: ')
    novo_nascimento = input('Informe a nova data de nascimento: ')
    novo_sexo = (input('Informe o novo sexo do aluno: ')).upper()
    cursor.execute('''UPDATE cadastro_alunos SET nome = ?, nascimento = ?, sexo = ? where matricula = ?''', (novo_nome, novo_nascimento, novo_sexo, matricula))
    cx.commit()
    print('Cadastro atualizado com sucesso!!!')
    dados_Alunos = cursor.execute('''select * from cadastro_alunos where matricula = ? ''', (matricula))
    print(dados_Alunos.fetchall())

def deletarAluno():
    matricula = input('informe o número de matrícula do aluno a ser excluído do banco de dados: ')
    cursor.execute('''Delete from cadastro_alunos where matricula = ? ''', (matricula))
    cx.commit()
    print(f'Cadastro de {matricula} deletado com sucesso!!!')
    dados_Alunos = cursor.execute('select * from cadastro_alunos;')
    rows = dados_Alunos.fetchall()
    for row in rows:
        print(row)   

opcao = int(input('''ESCOLHA UMA OPÇÃO DO MENU:
         (1) - LER LISTA DE ALUNOS
         (2) - ADICIONAR NOVO ALUNO
         (3) - ATUALIZAR/RETIFICAR CADASTRO ALUNO
         (4) - DELETAR CADASTRO ALUNO
         (0) - SAIR
'''))

while opcao != 0:
    if opcao == 1:
        lerListaAlunos()
    elif opcao == 2:
        adicionarAluno()
    elif opcao == 3:
        atualizarAluno()
    elif opcao == 4:
        deletarAluno()
    else:
        print('Encerrar programa!')

    opcao = int(input('''ESCOLHA UMA OPÇÃO DO MENU:
         (1) - LER LISTA DE ALUNOS
         (2) - ADICIONAR NOVO ALUNO
         (3) - ATUALIZAR/RETIFICAR CADASTRO ALUNO
         (4) - DELETAR CADASTRO ALUNO
         (0) - SAIR
'''))


    
















