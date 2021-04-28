''' 4) Escreva funções que realizem respectivamente as 
operações básicas de Create Read Update Delete para as 
duas novas tabelas.  '''
from os import path
from sqlite3 import dbapi2

db_file = path.join(path.dirname(path.abspath(__file__)), 'db3_alunos.db')
cx = dbapi2.connect(db_file)

cursor = cx.cursor()

def adicionarAluno():
    numero_id = int(input('Informe o número do aluno: '))
    nome_aluno = input('Informe o nome do aluno: ')
    data_nascimento = input('Informe a data de nascimento dd/mm/aaaa: ')
    sexo_aluno = (input('Informe o sexo do aluno (M/F): ')).upper()
    cursor.execute('''insert into alunos (id, nome, nascimento, sexo) values (?,?,?,?)''',
    (numero_id, nome_aluno, data_nascimento, sexo_aluno))
    cx.commit()

def lerListaAlunos():
    dados_Alunos = cursor.execute('select * from alunos;')
    rows = dados_Alunos.fetchall()
    for row in rows:
        print(row)

def atualizarAluno():
    numero_id = int(input('Informe o número do aluno para retificar: '))
    novo_nome = input('Informe o novo nome do aluno: ')
    novo_nascimento = input('Informe a nova data de nascimento: ')
    novo_sexo = (input('Informe o novo sexo do aluno: ')).upper()
    cursor.execute('''UPDATE alunos SET nome = ?, nascimento = ?, sexo = ? where id = ?''', (novo_nome, novo_nascimento, novo_sexo, numero_id))
    cx.commit()
    print('Cadastro atualizado com sucesso!!!')
    dados_Alunos = cursor.execute(f'''select * from alunos where id = {numero_id};''')
    print(dados_Alunos.fetchall())

def deletarAluno():
    numero_id = input('informe o número do aluno a ser excluído do banco de dados: ')
    cursor.execute(f'''delete from alunos where id = {numero_id}; ''')
    cx.commit()
    print(f'Cadastro de {numero_id} deletado com sucesso!!!')
    dados_Alunos = cursor.execute('select * from alunos;')
    rows = dados_Alunos.fetchall()
    for row in rows:
        print(row)   

def criar_Turma():
    id_turma = int(input('Informe o número da nova turma: '))
    codigo = int(input('Informe o código da turma: '))
    nome = input('Informe o nome da turma: ')
    cursor.execute('''insert into turmas (id, codigo_turma, nome_turma) values (?,?,?)''',(id_turma, codigo, nome))
    cx.commit()
    print(f'Turma de nome {nome} criada com sucesso!!!')
    dados_Turma = cursor.execute(f'select * from turmas where id = {id_turma};')
    print(dados_Turma.fetchone())

def ler_Turma():
    dados_Turma = cursor.execute('select * from turmas;')
    dados = dados_Turma.fetchall()
    for dado in dados:
        print(dado)

def atualizar_Turma():
    id_turma = int(input('Informe o número da nova turma para atualizar/retificar: '))
    codigo = int(input('Informe o novo código da turma: '))
    nome = input('Informe o novo nome da turma: ')
    cursor.execute('''UPDATE turmas SET codigo_turma = ?, nome_turma = ? where id = ?''', (codigo, nome, id_turma))
    cx.commit()
    print('Turma atualizada com sucesso!!!')
    dados_Turma = cursor.execute(f'''select * from turmas where id = {id_turma};''')
    print(dados_Turma.fetchone())

def deletar_Turma():
    id_turma = int(input('Informe o número da turma para deletar: '))
    cursor.execute('''delete from turmas where id = ?''', (id_turma))
    cx.commit()
    print(f'Turma {id_turma} deletada com sucesso!!!')

def matricular_Aluno():
    codigo_matricula = int(input('Informe o código da matrícula: '))
    aluno = input('Informe o id do aluno: ')
    turma = input('Informe a turma: ')
    ano = int(input('Informe o ano: '))
    periodo = input('Informe o período: ')
    cursor.execute('''insert into matriculas (cod_matricula, id_aluno, id_turma, ano, periodo) values (?,?,?,?,?)''',
    (codigo_matricula, aluno, turma, ano, periodo))
    cx.commit()
    dados_Matricula = cursor.execute(f'select * from matriculas where cod_matricula = {codigo_matricula};')
    print(dados_Matricula.fetchone())

def ler_Matriculas():
    dados_Matricula = cursor.execute('select * from matriculas;')
    for dado in dados_Matricula:
        print(dado)

def atualizar_Matricula():
    codigo_matricula = int(input('Informe o código da matrícula a ser atualizada/retificada: '))
    aluno = input('Informe o novo id do aluno: ')
    turma = input('Informe a nova turma: ')
    ano = int(input('Informe o novo ano: '))
    periodo = input('Informe o novo período: ')
    cursor.execute('''UPDATE matriculas set id_aluno=?, id_turma=?, ano=?, periodo=? where cod_matricula = ?''',
    (aluno, turma, ano, periodo, codigo_matricula))
    cx.commit()
    print(f'A atualização da matrícula {codigo_matricula} realizada com sucesso!!!')
    dados_Matricula = cursor.execute(f'select * from matriculas where cod_matricula = {codigo_matricula};')
    print(dados_Matricula.fetchone())

def deletar_Matricula():
    codigo_matricula = int(input('Informe o código da matrícula a ser deletada: '))
    cursor.execute('delete from matriculas where cod_matricula = ?', (codigo_matricula))
    cx.commit()
    print(f'A matrícula {codigo_matricula} foi deletada com sucesso!!!')

opcao = int(input('''ESCOLHA UMA OPÇÃO DO MENU:
         (1) - LER LISTA DE ALUNOS      (2) - ADICIONAR NOVO ALUNO
         (3) - ATUALIZAR CADASTRO ALUNO (4) - DELETAR CADASTRO ALUNO
         (5) - CRIAR NOVA TURMA         (6) - LER LISTA DE TURMAS
         (7) - ATUALIZAR TURMA          (8) - DELETAR TURMA
         (9) - MATRICULAR ALUNO         (10) - VER LISTA DE MATRÍCULAS
         (11) - ATUALIZAR MATRÍCULA     (12) - DELETAR MATRÍCULA
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
    elif opcao == 5:
        criar_Turma()
    elif opcao == 6:
        ler_Turma()
    elif opcao == 7:
        atualizar_Turma()
    elif opcao == 8:
        deletar_Turma()
    elif opcao == 9:
        matricular_Aluno()
    elif opcao == 10:
        ler_Matriculas()
    elif opcao == 11:
        atualizar_Matricula()
    elif opcao == 12:
        deletar_matricula()
    else:
        print('Encerrar programa!')

    opcao = int(input('''ESCOLHA UMA OPÇÃO DO MENU:
         (1) - LER LISTA DE ALUNOS      (2) - ADICIONAR NOVO ALUNO
         (3) - ATUALIZAR CADASTRO ALUNO (4) - DELETAR CADASTRO ALUNO
         (5) - CRIAR NOVA TURMA         (6) - LER LISTA DE TURMAS
         (7) - ATUALIZAR TURMA          (8) - DELETAR TURMA
         (9) - MATRICULAR ALUNO         (10) - VER LISTA DE MATRÍCULAS
         (11) - ATUALIZAR MATRÍCULA     (12) - DELETAR MATRÍCULA
         (0) - SAIR
         '''))
cursor.close()
cx.close()