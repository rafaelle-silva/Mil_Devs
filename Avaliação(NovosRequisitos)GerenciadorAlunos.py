import os
from datetime import datetime,date,time
import locale

def imprimirMenu():
    os.system('cls')
    print("=" * 40 + " Gerenciamento de Alunos " + "=" * 40)
    print("1 - Inserir aluno")
    print("2 - Excluir aluno por código")
    print("3 - Exibir dados do aluno por código")
    print("4 - Listar todos os alunos")
    print("5 - Lançar nota Prova 1")
    print("6 - Lançar nota Prova 2")
    print("7 - Lançar nota Trabalho 1")
    print("8 - Lançar nota Trabalho 2")
    print("9 - Lançar nota Recuperação")
    print("10 - Sair")
    print("=" * 104)

def ModelosDados():
    espacos = 16 * " "
    print(f"Código{espacos}", end="")
    print("Nome   ", end="")
    print("Prova1   ", end="")
    print("Prova2   ", end="")
    print("Trab1   ", end="")
    print("Trab2   ", end="")
    print("NotaREC   ", end="")
    espacos = 6 * " "
    print(f"Nota Final{espacos}", end="")
    print(f"Status")

def CalculaNotaFinal(codigoAluno,memoria):
    prova1 = memoria[codigoAluno][3]
    prova2 = memoria[codigoAluno][4]
    trab1 = memoria[codigoAluno][5]
    trab2 = memoria[codigoAluno][6]

    if prova1 == None and prova2 == None and trab1 == None and trab2 == None:
        pass
    else:
        NotaFinal = ((int(prova1) + int(prova2)) / 2 ) * 0.7 + ((int(trab1) + int(trab2))  / 2 ) * 0.3
        return round(NotaFinal,2)

def CalculaStatus(notaFinal):
    if notaFinal == None:
        pass
    else:
        if notaFinal >= 6:
            status = 'Aprovado'
        elif notaFinal >= 5 and notaFinal <= 5.9 :
            status = 'Recuperação'
        else:
            status = 'Reprovado'
        return status

def ValidaNotaRec(notaRec,NotaFinal):
    if notaRec == None and NotaFinal == None:
        pass
    else:
        if notaRec > NotaFinal:
            NotaFinal = notaRec
            return NotaFinal

def ValidaStatus(NotaFinal):
    if NotaFinal == None:
        pass
    else:
        if NotaFinal >= 6:
            status = 'Aprovado'
            return status
        else:
            status = 'Reprovado'
            return status

####################################################################

def insereAluno(memoria):
    aluno = []
    codigoAluno = 0
    for i in range(len(memoria)):
        codigoAluno += 1
    aluno.append(codigoAluno)
    nome = input('Nome do aluno: ')
    print('Para a inserção da data de nascimento do aluno, informe: ')
    ano = int(input('Ano: '))
    mes = int(input('Mês: '))
    dia = int(input('Dia: '))
    dataNascimento = date(year=ano, month=mes, day=dia)

    locale.setlocale(locale.LC_TIME, "pt_BR")
    dataFormatada = dataNascimento.strftime('%A, %d de %B de %Y')

    aluno.append(nome)

    resposta = input('Deseja lançar também as notas P1, P2, T1 e T2? S/N  ')
    validada = resposta.upper()
    if validada == 'S':
        aluno.append(float(input('Insira a nota da prova 1: ')))
        aluno.append(float(input('Insira a nota da prova 2: ')))
        aluno.append(float(input('Insira a nota do trabalho 1: ')))
        aluno.append(float(input('Insira a nota do trabalho 2: ')))
        aluno.append(None)
        aluno.append(None)
        aluno.append(None)
        aluno.append(dataFormatada)
    else:
        aluno.append(None)
        aluno.append(None)
        aluno.append(None)
        aluno.append(None)
        aluno.append(None)
        aluno.append(None)
        aluno.append(None)
        aluno.append(dataFormatada)
    memoria.append(aluno)
    return memoria

def excluirAluno(memoria):
    codigo_aluno = int(input('Informe código do aluno: '))
    memoria.pop(codigo_aluno-1)
    return memoria

def exibir_AlunoporCodigo(memoria):
    codigoAluno = int(input('Insira o código do aluno, por favor: '))
    ModelosDados()
    posicao = memoria[codigoAluno-1]
    notaFinal = CalculaNotaFinal(codigoAluno-1, memoria)
    status = CalculaStatus(notaFinal)

    if status == 'Recuperação' and posicao[7] != "-":
        notaFinal = ValidaNotaRec(posicao[7], notaFinal)
        status = ValidaStatus(notaFinal)
    else:
        pass

    if posicao[3] == None or posicao[4] == None or posicao[5] == None or posicao[6] == None:
        print(f'{posicao[0]}{21 * " "}', end=" ")
        print(f'{posicao[1]}{5 * " "}', end=" ")
        print(f'{posicao[2]}{5 * " "}', end=" ")
        print(f' - {5 * " "}', end=" ")
        print(f' - {5 * " "}', end=" ")
        print(f' - {4 * " "}', end=" ")
        print(f' - {10 * " "}', end=" ")
        print(f' - {8 * " "}', end=" ")
        print(f' - {8 * " "}', end=" ")
        print(' - ')
    else:
        print(f'{posicao[0]}{21 * " "}', end=" ")
        print(f'{posicao[1]}{5 * " "}', end=" ")
        print(f'{posicao[2]}{5 * " "}', end=" ")
        print(f'{posicao[3]}{5 * " "}', end=" ")
        print(f'{posicao[4]}{4 * " "}', end=" ")
        print(f'{posicao[5]}{10 * " "}', end=" ")
        print(f'{posicao[6]}{10 * " "}', end=" ")
        print(f'{notaFinal}{8 * " "}', end=" ")
        print(status)

def listar_Alunos(memoria):
    ModelosDados()
    cont = 1
    for posicao_aluno in memoria:
        notaFinal = CalculaNotaFinal(cont - 1, memoria)
        status = CalculaStatus(notaFinal)
        if status == 'Recuperação' and posicao_aluno[7] != "-":
            notaFinal = ValidaNotaRec(posicao_aluno[7], notaFinal)
            status = ValidaStatus(notaFinal)


        if posicao_aluno[3] == None and posicao_aluno[4] == None and posicao_aluno[5] == None and posicao_aluno[6] == None:
            print(f'{posicao_aluno[0]}{18 * " "}', end=" ")
            print(f'{posicao_aluno[1]}{5 * " "}', end=" ")
            print(f'{posicao_aluno[2]}{5 * " "}', end=" ")
            print(f' - {5 * " "}', end=" ")
            print(f' - {5 * " "}', end=" ")
            print(f' - {4 * " "}', end=" ")
            print(f' - {4 * " "}', end=" ")
            print(f' - {4 * " "}', end=" ")
            print(f' - {4 * " "}', end=" ")
            print(f' - {4 * " "}', end=" ")
            print(' - ')
        else:
            print(f'{posicao_aluno[0]}{5 * " "}', end=" ")
            print(f'{posicao_aluno[1]}{5 * " "}', end=" ")
            print(f'{posicao_aluno[2]}{5 * " "}', end=" ")
            print(f'{posicao_aluno[3]}{5 * " "}', end=" ")
            print(f'{posicao_aluno[4]}{4 * " "}', end=" ")
            print(f'{posicao_aluno[5]}{10 * " "}', end=" ")
            print(f'{posicao_aluno[6]}{10 * " "}', end=" ")
            if posicao_aluno[7] == None:
                print(f' - ', end=" ")
            else:
                print(f'{posicao_aluno[7]}', end=" ")
            print(f'{notaFinal}{8 * " "}', end=" ")
            print(status)
        cont += 1

def lancar_Nota1(memoria):
    cod_aluno = int(input('Insira código do aluno:  '))
    nota1 = float(input('Insira a nota da prova 1:  '))
    memoria[cod_aluno-1][3] = nota1

def lancar_Nota2(memoria):
    cod_aluno = int(input('Insira código do aluno:  '))
    nota2 = float(input('Insira a nota da prova 2: '))
    memoria[cod_aluno-1][4] = nota2

def lancar_trab1(memoria):
    cod_aluno = int(input('Insira código do aluno para exclusão:  '))
    trab1 = float(input('Insira a nota do trabalho 1: '))
    memoria[cod_aluno-1][5] = trab1

def lancar_trab2(memoria):
    cod_aluno = int(input('Insira código do aluno para exclusão:  '))
    trab2 = float(input('Insira a nota do trabalho 2: '))
    memoria[cod_aluno-1][6] = trab2

def lancar_notaREC(memoria):
    cod_aluno = int(input('Insira código do aluno: '))
    notaFinal = CalculaNotaFinal(cod_aluno-1,memoria)
    status = CalculaStatus(notaFinal)
    if status == 'Recuperação':
        notaREC = float(input('Insira a nota de recuperação: '))
        memoria[cod_aluno-1][7] = notaREC
    else:
        print('Aluno não está de recuperação!')

codigoAluno = 0
memoria = []

while(1):
    imprimirMenu()
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        insereAluno(memoria)
    elif opcao == 2:
        excluirAluno(memoria)
    elif opcao == 3:
        exibir_AlunoporCodigo(memoria)
    elif opcao == 4:
        listar_Alunos(memoria)
    elif opcao == 5:
        lancar_Nota1(memoria)
    elif opcao == 6:
        lancar_Nota2(memoria)
    elif opcao == 7:
        lancar_trab1(memoria)
    elif opcao == 8:
        lancar_trab2(memoria)
    elif opcao == 9:
        lancar_notaREC(memoria)
    elif opcao == 10:
        for dados in range(len(memoria)):
            dados = memoria[0]
        dados = str(dados)
        with open('dados.txt', 'w') as f:
            f.write(' '.join(dados))
        break
    else:
        print('Opção Inválida, tente novamente...')

