import platform
import os
import re

def limpaTela():
    so = platform.system()
    print(so)
    if so == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        print("\x1b[2J")

def validarTelefone(numero):
    ret = False
    pattern = "^[0-9]{2}-[0-9]{9}$"
    if re.match(pattern,numero) != None:
        ret = True
    return ret

def retornaListaMatricula(alunos):
    matriculaLista = list()
    for aluno in alunos:
        matriculaLista.append(aluno["matricula"])
    return matriculaLista

def retornaNomeAluno(matricula, alunos):
    nome = ''
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            nome = aluno["nome"]
            break
    return str(nome)

def retornaDicionarioNota(matricula, notas):
    achou = False
    nota = dict()
    for x in notas:
        if x["matricula"] == matricula:
            achou = True
            nota = x
            break
    if not achou:
        nota["matricula"] = matricula
    return nota

def dicionarioNotaExiste(matricula, notas):
    ret = False
    for nota in notas:
        if nota["matricula"] == matricula:
            ret = True
    return ret

def retornaDicionarioAluno(matricula, alunos):
    aluno = dict()
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            break
    return aluno

def ehNotaValida(nota):
    ret = False
    if not nota.isalpha():
        nota = float(nota)
        if nota >= 0 and nota <= 10:
            ret = True
    return ret

def retornaQuantidadeAlunos(alunos):
    ret = 0
    for aluno in alunos:
        ret += 1
    return ret

def retornaPercentualAprovados(quantidade, notas):
    #para ser aprovado a media deve ser superior a 7 ou a recuperação deve ser superior a 7
    print(notas)
    quant_aprovados = 0
    percentual = 0
    for nota in notas:
        ad1 = float(nota.get("ad1","-1"))
        ad2 = float(nota.get("ad2","-1"))
        recuperacao = float(nota.get("recuperacao","-1"))
        if ad1 > -1 and ad2 > -1:
            media = (ad1 + ad2) / 2
            if media < 7:
                if recuperacao >= 7:
                    quant_aprovados += 1
            else:
                quant_aprovados += 1
    if quant_aprovados > 0:
        percentual = (quant_aprovados * 100) / quantidade
    return percentual

def retornaMatriculaMaiorMedia(notas):
    matricula = 0
    media_geral = 0
    for nota in notas:
        ad1 = float(nota.get("ad1","-1"))
        ad2 = float(nota.get("ad2","-1"))
        recuperacao = float(nota.get("recuperacao","-1"))
        if ad1 > -1 and ad2 > -1:
            media = (ad1 + ad2) / 2
            if media > media_geral:
                matricula = nota.get("matricula","-1")
                media_geral = media
            if media < 7:
                if recuperacao > media_geral:
                    matricula = nota.get("matricula","-1")
                    media_geral = recuperacao
    return matricula

def retornaMediaTurma(quantidade, notas):
    media_geral = 0
    media = 0
    for nota in notas:
        ad1 = float(nota.get("ad1","-1"))
        ad2 = float(nota.get("ad2","-1"))
        recuperacao = float(nota.get("recuperacao","-1"))
        if ad1 > -1 and ad2 > -1:
            media = (ad1 + ad2) / 2
        if media < 7 and recuperacao > -1:
            media = recuperacao
        media_geral += media
    return media_geral / quantidade