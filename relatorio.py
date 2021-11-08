from util import retornaQuantidadeAlunos
from util import retornaPercentualAprovados
from util import retornaMatriculaMaiorMedia
from util import retornaMediaTurma

def gerarFrequencia(alunos):
    print('|' + '-' * 118 + '|')
    print(f'| {"LISTA DE FREQUENCIA".center(116)} |')
    print('|' + '-' * 118 + '|')
    print(f'|{"MATRICULA".center(11)} | {"ALUNO".center(40)} | {"ASSINATURA".center(60)} |')
    for aluno in alunos:
        matricula = "00" + str(aluno["matricula"])
        print(f'|{matricula[-3:].center(11)} | {aluno["nome"].title().ljust(40)} | ____________________________________________________________ |')
    print('|' + '-' * 118 + '|')

def gerarNotas(alunos, notas):
    print('|' + '-' * 111 + '|')
    print(f'| {"RELATÓRIO DE NOTAS".center(109)} |')
    print('|' + '-' * 111 + '|')
    print(f'|{"MATRICULA".center(11)} | {"ALUNO".center(40)} | {"AD1".center(10)} | {"AD2".center(10)} | {"MÉDIA".center(10)} | {"RECUPERAÇÃO".center(14)} |')
    for aluno in alunos:
        matricula = "00" + str(aluno["matricula"])
        ad1 = "-"
        ad2 = "-"
        recuperacao = "-"
        media = "-"
        for nota in notas:
            if nota["matricula"] == aluno["matricula"]:
                ad1 = str(nota.get("ad1","-"))
                ad2 = str(nota.get("ad2","-"))
                if ad1 != "-" and ad2 != "-":
                    media = str((float(ad1) + float(ad2)) / 2)
                recuperacao = str(nota.get("recuperacao","-"))
        print(f'|{matricula[-3:].center(11)} | {aluno["nome"].title().ljust(40)} | {ad1.rjust(10)} | {ad2.rjust(10)} | {media.rjust(10)} | {recuperacao.rjust(14)} |')
    print('|' + '-' * 111 + '|')

def gerarResumo(alunos, notas):
    totalAlunos = retornaQuantidadeAlunos(alunos)
    aprovados = 0
    reprovados = 0
    matricula = 0
    media_geral = 0.0
    if totalAlunos > 0:
        aprovados = round(retornaPercentualAprovados(totalAlunos, notas),2)
        reprovados = round(100.0 - aprovados,2)
        matricula = retornaMatriculaMaiorMedia(notas)
        media_geral = round(retornaMediaTurma(totalAlunos, notas),2)
    print('|' + '-' * 44 + '|')
    print(f'| {"RESUMO DO CURSO".center(42)} |')
    print('|' + '-' * 44 + '|')
    print(f'| \033[36m\033[1mTOTAL DE ALUNOS CADASTRADOS:\033[0;0m \t\t{str(totalAlunos).rjust(6)}\t |')
    print(f'| \033[36m\033[1mTOTAL DE ALUNOS APROVADOS (%):\033[0;0m \t{str(aprovados).rjust(6)}\t |')
    print(f'| \033[36m\033[1mTOTAL DE ALUNOS REPROVADOS (%):\033[0;0m \t{str(reprovados).rjust(6)}\t |')
    print(f'| \033[36m\033[1mMATRÍCULA COM MAIOR MÉDIA FINAL:\033[0;0m \t{str(matricula).rjust(6)}\t |')
    print(f'| \033[36m\033[1mMÉDIA GERAL DA TURMA:\033[0;0m \t\t\t{str(media_geral).rjust(6)}\t |')
    print('|' + '-' * 44 + '|')
