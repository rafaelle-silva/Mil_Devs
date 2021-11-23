import os

class Contato:

    status=True

    def __init__(self,nome, email, telefoneFixo, telefoneCelular):
        self.nome = nome
        self.email = email
        self.telefoneFixo = telefoneFixo
        self.telefoneCelular = telefoneCelular

class Agenda:

    __contatos=[]

    def exibirMenu(self):
        os.system('clear')
        print("=" * 40 + " MENU " + "=" * 40)
        print("0 - Sair do sistema")
        print("1 - Adicionar contato")
        print("2 - Pesquisar contato")
        print("3 - Editar contato")
        print("4 - Excluir contato")
        print("5 - Excluir todos os contatos")
        print("6 - Imprmir Lista de contato")
        print("7 - Bloquear contato")
        print("8 - Desbloquear contato")
        print("=" * 86)

    def adicionarContato(self):
        os.system('clear')
        nome = input("Digite o nome do contato: ")
        email = input("Digite o email: ")
        fixo = input("Digite o telefone fixo: ")
        celular = input("Digite o telefone celular: ")
        contato = Contato(nome,email,fixo,celular)
        self.__contatos.append(contato)

    def mostrarContato(self,contact):
        print('='*64)
        print("Contato "+str(self.__contatos.index(contact)+1))
        print(f'Nome = {contact.nome}')
        print(f'Email = {contact.email}')
        print(f'Telefone Celular = {contact.telefoneCelular}')
        print(f'Telefone Fixo = {contact.telefoneFixo}')
        if(contact.status):
            print(f'Status = Ativo')
        else:
            print(f'Status = Bloqueado')
        print('=' * 64)

    def exibirContatos(self):
        for contato in self.__contatos:
            self.mostrarContato(contato)

    def exibirMenuPesquisa(self):
        os.system('clear')
        print("=" * 40 + " MENU PESQUISA " + "=" * 40)
        print("0 - Voltar para o programa principal")
        print("1 - Pesquisar por nome")
        print("2 - Pesquisar por telefone fixo")
        print("3 - Pesquisar por telefone celular")
        print("4 - Pesquisar por email")
        print("=" * 86)

    def pesquisaPorNome(self):
        os.system('clear')
        nome = input("Digite o nome a ser pesquisado: ")
        encontrouContato = False

        for contato in self.__contatos:
            if(contato.nome.lower() == nome.lower()):
                self.mostrarContato(contato)
                encontrouContato = True
                break

        if(encontrouContato == False):
            print("Não foram encontrados contatos com este nome!")

    def pesquisaPorTelefoneFixo(self):
        os.system('clear')
        fixo = input("Digite o Telefone Fixo a ser pesquisado: ")
        encontrouContato = False

        for contato in self.__contatos:
            if(contato.telefoneFixo.lower() == fixo.lower()):
                self.mostrarContato(contato)
                encontrouContato = True

        if(encontrouContato == False):
            print("Não foram encontrados contatos com este telefone Fixo!")

    def pesquisaPorTelefoneCelular(self):
        os.system('clear')
        celular = input("Digite o Telefone Celular a ser pesquisado: ")
        encontrouContato = False

        for contato in self.__contatos:
            if(contato.telefoneCelular.lower() == celular.lower()):
                self.mostrarContato(contato)
                encontrouContato = True
                break

        if(encontrouContato == False):
            print("Não foram encontrados contatos com este telefone celular!")

    def pesquisaPorEmail(self):
        os.system('clear')
        email = input("Digite o email a ser pesquisado: ")
        encontrouContato = False

        for contato in self.__contatos:
            if(contato.email.lower() == email.lower()):
                self.mostrarContato(contato)
                encontrouContato = True
                break

        if(encontrouContato == False):
            print("Não foram encontrados contatos com este email!")

    def bloquearContato(self):
        print("Para bloquear um contato, é necessário informar o CodigoContato.")
        resposta = input("Você sabe o CodigoContato? [s/n]: ")

        # caso o usuario digite sim ou nao ao invez de s ou n, pegamos somente a posicao 0 do texto
        if resposta.lower()[0] == "s":
            posicao = int(input("Digite o código do contato: "))
            try:
                self.__contatos[posicao-1].status = False
                print("Usuário bloqueado com sucesso.", end=" ")
            except IndexError:
                print("Codigo do contato não existe!", end=" ")
        else:
            self.exibirContatos()
            print("Para descobrir o Codigo do Contato acesse a opção ")
            print("'Imprmir Lista de contato' do menu principal")

        input("Tecle ENTER para continuar.")

    def editarContato(self):
        contact_id = int(input("Digite o id do contato a ser alterado : "))

        if(contact_id>len(self.__contatos)):
            print("Contato inválido... tente novamente.")
            return

        nome = input("Digite o nome do contato : ")
        email = input("Digite o email do contato : ")
        fixo = input("Digite o telefone fixo do contato : ")
        celular = input("Digite o telefone celular do contato : ")

        self.__contatos[contact_id-1].nome = nome
        self.__contatos[contact_id-1].email = email
        self.__contatos[contact_id-1].telefoneFixo = fixo
        self.__contatos[contact_id-1].telefoneCelular = celular
        print("Contato editado com sucesso !!!")
        input("Digite ENTER para continuar !!!")

    def excluirContato(self):
        contact_id = int(input("Digite o id do contato a ser excluido : "))

        if(contact_id>len(self.__contatos)):
            print("Contato inválido... tente novamente.")
            return

        del agenda.__contatos[contact_id-1]

        print("Contato excluido com sucesso!!")
        input("Digite ENTER para continuar !!!")

    def excluiTodosContatos(self):
        print("Deseja mesmo excluir todos os contatos? ( sim / nao ) ")

        op = input()

        if(op[0].lower() == "s"):
            self.__contatos = []
            print("Lista de contatos vazia")

        else:
            print("Operação cancelada...")

        input("Digite ENTER para continuar !!!")

    def desbloqueaContato(self):
        contact_id = int(input("Digite o id do contato a ser desbloqueado : "))

        if(contact_id>len(self.__contatos)):
            print("Contato inválido... tente novamente.")
            return

        if(agenda.__contatos[contact_id-1].status == False):
            agenda.__contatos[contact_id - 1].status = True
            print("Contato desbloqueado com sucesso !!")
        else:
            print("Este contato não está bloqueado...")
        input("Digite ENTER para continuar !!!")

agenda = Agenda()

while(True):

    agenda.exibirMenu()
    opcao = int(input("Digite a opção desejada: "))

    if (opcao == 0):  # sair do programa
        print("Até logo :-)")
        break
    elif (opcao == 1):  # Adicionar contato
        agenda.adicionarContato()
    elif (opcao == 2):  # Menu Pesquisa
        agenda.exibirMenuPesquisa()
        opcao = int(input("Digite a opção desejada: "))
        if (opcao == 1):  # Pequisa por nome
            agenda.pesquisaPorNome()
        elif (opcao == 2):  # pesquisa por telefone fixo
            agenda.pesquisaPorTelefoneFixo()
        elif (opcao == 3):  # pesquisa por telefone celular
            agenda.pesquisaPorTelefoneCelular()
        elif (opcao == 4):  # pesquisa por email
            agenda.pesquisaPorEmail()
        # colocamos este input apenas para fazer com que o sistema fique
        # parado e de tempo do usuario ler os resultados impressos
        input("\nTecle ENTER para continuar!")
    elif (opcao == 3):
        agenda.editarContato()
    elif ( opcao == 4):
        agenda.excluirContato()
    elif ( opcao == 5):
        agenda.excluiTodosContatos()
    elif (opcao == 6):  # Exibe os contatos
        os.system('clear')
        agenda.exibirContatos()
        input("\nTecle ENTER para continuar!")
    elif (opcao == 7):  # bloquear contato
        os.system('clear')
        agenda.bloquearContato()
    elif (opcao == 8):
        agenda.desbloqueaContato()
    else:
        print("Opção inválida.. tente novamente")
        os.system('clear')
