#Faça um algoritmo que leia um número que represente a quantidade de alunos que devem ser lidos. 
#Para cada aluno, leia o nome uma nota (de 0 a 10) para: trabalho 1, prova 1, trabalho 2, prova 2. 
#Após a leitura dos dados a média final com base na formula ((((Trab1 + Trab2)/2)*3) + (((Prova1 + Prova2)/2)*7))/10



qtdeAlunos = int(input("Digite a quantidade de alunos a ser lido: "))

nomes = []
provas1 = [] 
provas2 = []
trabalhos1 = []
trabalhos2 = []
mediasFinal = []
status = []

for i in (range(qtdeAlunos)):
    nome = input("Digite o nome do aluno: ")
    prova1 = float(input("Digite a nota da prova 1: "))
    prova2 = float(input("Digite a nota da prova 2: "))
    trabalho1 = float(input("Digite a nota do trabalho 1: "))
    trabalho2 = float(input("Digite a nota da trabalho 2: "))

    nomes.append(nome)
    provas1.append(prova1)
    provas2.append(prova2)
    trabalhos1.append(trabalho1)
    trabalhos2.append(trabalho2)
    print("")

#imprimindo o titulo da tabela
espaco_nome = 16 * " "
print(f"Nome{espaco_nome}",end="")
print("Trab1 ", end="")
print("Prova1 ",end="")
print("Trab2 ",end="")
print("Prova2   ", end="")
espacos = 6 * " "
print(f"Nota Final{espacos}", end="")
print(f"Resultado Final")

for i in (range(len(nomes))):
    resultado = ((((trabalhos1[i] + trabalhos2[i])/2)*3) + (((provas1[i] + provas2[i])/2)*7))/10
    mediasFinal.append(resultado)

    if resultado < 5:
        status.append("Reprovado")
    elif resultado >= 5 and resultado < 6:
        status.append("Recuperacao")
    else:
        status.append("Aprovado")

    if len(nomes[i]) >= 19:
        print(f"{nomes[i][:16]}... ",end="")
    else:
        qtdeEspacos = len(nomes[i])
        espacos = " " * (20 - qtdeEspacos)
        print(f"{nomes[i]}{espacos}", end="")

    qtdeEspacos = len(str(trabalhos1[i]))
    #espacos = " " * (5 - qtdeEspacos)
    espaco1 = 3 * " "
    espaco_prov1_trab2 = 4 * " "
    espaco_pro2_medf = 6 * " "
    espaco_medf = 15 * " "

    print(f"{trabalhos1[i]}{espaco1}",end="")
    print(f'{provas1[i]}{espaco_prov1_trab2}', end="")
    print(f'{trabalhos2[i]}{espaco1}', end="")
    print(f'{provas2[i]}{espaco_pro2_medf}', end="")
    print(f'{round(mediasFinal[i],1)}{espaco_medf}', end="")
    print(f'{status[i]} ')
