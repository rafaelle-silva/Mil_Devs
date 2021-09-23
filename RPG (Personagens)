class Personagem:

    vida = 150
    mana = 100
    inteligencia = 30
    forca = 30
    agilidade = 30
    carisma = 20

    def __init__(self,nome):
        self.nome = nome


    def atacar(self,inimigo):
        inimigo.vida -= self.forca
        print(f'{self.nome} tirou {self.forca} pontos de vida de {inimigo.nome}')

class Guerreiro(Personagem):

    forca = 80
    inteligencia = 10
    agilidade = 20

    def esmagar(self,inimigo):
        inimigo.vida -= 2*self.forca
        print(f'{self.nome} ESMAGOU {inimigo.nome} tirando {2*self.forca} pontos de vida')

class Mago(Personagem):

    inteligencia = 80
    forca = 10
    agilidade = 20

    def magia(self,inimigo):
        inimigo.vida -= 2*self.inteligencia
        print(f'{self.nome} lançou uma bola de fogo em {inimigo.nome} tirando {2*self.inteligencia} pontos de vida')


class Bardo(Personagem):

    carisma = 70
    inteligencia = 20
    forca = 10
    agilidade = 20

    def curar(self,aliado):
        aliado.vida += 2*self.carisma
        print(f'{self.nome} restaurou  {2 * self.carisma} pontos de vida de {aliado.nome}')



class Arqueiro(Personagem):

    agilidade = 80
    forca = 20
    inteligencia = 20
    carisma = 10

    def flechar(self,inimigo):
        inimigo.vida -= 2*self.agilidade
        print(f'{self.nome} lançou uma flecha em {inimigo.nome} tirando {2*self.agilidade} pontos de vida')



g1 = Guerreiro("Leonidas")
m1 = Mago("Patolino")
b1 = Bardo("Miguel")
a1 = Arqueiro("Legolas")

print(type(g1))
