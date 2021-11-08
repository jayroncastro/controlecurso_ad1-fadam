from menu import menuPrincipal
from menu import menuRelatorios
from menu import informMatriculaInvalida
from aluno import cadastrar
from aluno import lancarNotas
from aluno import exibir
from aluno import editar
from aluno import excluir
from util import retornaListaMatricula
from util import retornaNomeAluno
from util import retornaDicionarioNota
from util import retornaDicionarioAluno
from util import dicionarioNotaExiste
from relatorio import gerarFrequencia
from relatorio import gerarNotas
from relatorio import gerarResumo

alunos = list()
notas = list()
opcao = 0
while True:
    menuPrincipal()
    opcao = input('Selecione uma opção: ')
    if opcao.isnumeric():
        opcao = int(opcao)
        if opcao == 99:
            print('\033[32mObrigado por usar nosso aplicativo\033[0;0m\n\033[34m>> A FADAM AGRADECE <<\033[0;0m')
            break
        elif opcao == 1: #cadastrar
            alunos.append(cadastrar(retornaListaMatricula(alunos)))
        elif opcao in (2,3,4,5):
            matricula = input('Informe a matrícula do aluno: ')
            if matricula.isnumeric():
                matricula = int(matricula)
                if retornaListaMatricula(alunos).count(matricula) > 0:
                    if opcao == 2: #buscar
                        exibir(retornaDicionarioAluno(matricula,alunos),retornaDicionarioNota(matricula,notas))
                    elif opcao == 3: #editar
                        alunos = editar(matricula, alunos)
                    elif opcao == 4: #excluir
                        exc = str(input(f'Você deseja realmente excluir o aluno \033[31m{retornaNomeAluno(matricula, alunos).upper()}\033[0;0m? Pressione [S] para SIM'))
                        if exc in ('S','s'):
                            alunos = excluir(matricula, alunos)
                            input('\033[32mProcesso de exclusão realizado com sucesso, pressione qualquer tecla para continuar...\033[0;0m')
                        else:
                            input('\033[31mO processo de exclusão foi cancelado, pressione qualquer tecla para continuar...\033[0;0m')
                    elif opcao == 5: #lancar notas
                        if not dicionarioNotaExiste(matricula,notas):
                            notas.append(lancarNotas(matricula, retornaNomeAluno(matricula, alunos), retornaDicionarioNota(matricula,notas)))
                        else:
                            lancarNotas(matricula, retornaNomeAluno(matricula, alunos), retornaDicionarioNota(matricula,notas))
                else:
                    informMatriculaInvalida()
        elif opcao == 6: #relatórios
            while True:
                menuRelatorios()
                opcao = input('Informe a opção: ')
                if opcao.isnumeric():
                    opcao = int(opcao)
                    if opcao == 99:
                        break
                    elif opcao == 1:
                        gerarFrequencia(alunos)
                    elif opcao == 2:
                        gerarNotas(alunos, notas)
                    elif opcao == 3:
                        gerarResumo(alunos, notas)
                    if opcao in (1,2,3):
                        input('Pressione qualquer tecla para continuar...')
                        break