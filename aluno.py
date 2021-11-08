from util import validarTelefone
from util import ehNotaValida
from menu import menuNotas
from menu import informRecuperacao

def cadastrar(chaves):
    aluno = dict()
    while True:
        matricula = input('Entre com a matricula do aluno: ')
        if matricula.isnumeric():
            matricula = int(matricula)
            if matricula > 0:
                aluno["matricula"] = matricula
                if chaves.count(matricula) == 0:
                    aluno["nome"] = input('Entre com o nome do aluno: ')
                    while True:
                        telefone = input('Entre com o telefone celular do aluno 99-999999999: ')
                        if validarTelefone(telefone):
                            aluno["telefone"] = telefone
                            break
                    aluno["endereco"] = input('Entre com o endereço do aluno: ')
                    break
                else:
                    print('\033[31m'+'ERRO - A matricula informada já está cadastrada'+'\033[0;0m')
                    opcao = input('ENTER para continuar ou 99 para voltar: ')
                    if opcao.isnumeric():
                        opcao = int(opcao)
                        if opcao == 99:
                            break
    return aluno

def lancarNotas(matricula, nome, nota):
    while True:
        print(f'Lançar notas do aluno \033[32m{nome.upper()}\033[0;0m com matrícula \033[32m{matricula}\033[0;0m: ')
        menuNotas()
        opcao = input('Informe a opção: ')
        if opcao.isnumeric():
            opcao = int(opcao)
            if opcao == 99:
                break
            elif opcao == 1: #lancar AD1
                ad1 = input('Entre com a nota da AD1: ')
                if ehNotaValida(ad1):
                    nota.update({"ad1":float(ad1)})
            elif opcao == 2: #lancar AD2
                ad2 = input('Entre com a nota da AD2: ')
                if ehNotaValida(ad2):
                    nota.update({"ad2":float(ad2)})
            elif opcao == 3: #lancar Recuperação
                ad1 = nota.get("ad1","-1")
                ad2 = nota.get("ad2","-1")
                if (ad1 != "-1") and (ad2 != "-1"):
                    media = float((ad1 + ad2) / 2)
                    if media < 7.0:
                        recuperacao = input('Entre com a nota de recuperação: ')
                        if ehNotaValida(recuperacao):
                            nota.update({"recuperacao":float(recuperacao)})
                    else:
                        informRecuperacao()
                else:
                    informRecuperacao()
    return nota

def exibir(aluno, nota):
    print('\033[36m-=\033[0;0m' * 18)
    print('\033[36m|          DADOS PESSOAIS          |\033[0;0m')
    print('\033[36m-=\033[0;0m' * 18)
    print(f'\033[36mMATRÍCULA:\033[0;0m\t \033[33m{aluno["matricula"]}\033[0;0m')
    print(f'\033[36mNOME:\033[0;0m\t\t \033[33m{aluno["nome"]}\033[0;0m')
    print(f'\033[36mTELEFONE:\033[0;0m\t \033[33m{aluno["telefone"]}\033[0;0m')
    print(f'\033[36mENDEREÇO:\033[0;0m\t \033[33m{aluno["endereco"]}\033[0;0m')
    print('\033[36m-=\033[0;0m' * 18)
    print('\033[36m|               NOTAS              |\033[0;0m')
    print('\033[36m-=\033[0;0m' * 18)
    print(f'\033[36mAD1:\033[0;0m\t\t \033[33m{nota.get("ad1","Não existe nota lançada")}\033[0;0m')
    print(f'\033[36mAD2:\033[0;0m\t\t \033[33m{nota.get("ad2","Não existe nota lançada")}\033[0;0m')
    print(f'\033[36mRECUPERAÇÃO:\033[0;0m \033[33m{nota.get("recuperacao","Não existe nota lançada")}\033[0;0m')
    input('Pressione qualquer tecla para continuar.')

def editar(matricula, alunos):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print('\033[1m'+'\033[31mPressione ENTER caso não queira alterar o valor\033[0;0m')
            print(f'\033[36mNOME ATUAL:\033[0;0m \033[33m{aluno["nome"]}\033[0;0m')
            nome = input('Altere o nome do aluno:')
            if len(nome) != 0:
                aluno["nome"] = nome
            while True:
                print(f'\033[36mCELULAR ATUAL:\033[0;0m \033[33m{aluno["telefone"]}\033[0;0m')
                telefone = input('Altere o telefone celular do aluno 99-999999999: ')
                if len(telefone) != 0:
                    if validarTelefone(telefone):
                        aluno["telefone"] = telefone
                        break
                else:
                    break
            print(f'\033[36mENDEREÇO ATUAL:\033[0;0m \033[33m{aluno["endereco"]}\033[0;0m')
            endereco = input('Altere o endereço do aluno: ')
            if len(endereco) != 0:
                aluno["endereco"] = endereco
            break
    return alunos

def excluir(matricula, alunos):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            break
    return alunos