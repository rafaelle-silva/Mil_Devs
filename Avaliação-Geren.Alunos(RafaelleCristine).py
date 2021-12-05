arquivo = open('dados.txt','a')
arquivo.write('Teste')
arquivo = open('dados.txt' , 'r')
print(arquivo.readlines())