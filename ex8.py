'''Classe Macaco: Desenvolva uma classe Macaco, que 
possua os atributos nome e bucho (estomago) e pelo 
menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, 
criando pelo menos dois macacos, alimentando-os 
com pelo menos 3 alimentos diferentes e verificando 
o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. 
É possível criar um macaco canibal? '''

class Macaco:
    def __init__(self, nome):
        self.nome = nome 
        self.bucho = []

    def comer(self, comida):
        if type(comida) != str:
            print('Não é possível comer isso.')
        else:
            self.bucho.append(comida.title())

    def verBucho(self):
        return self.bucho
    
    def digerir(self):
        self.bucho = []

macaco1 = Macaco('Mamaco')
macaco2 = Macaco('Bill')

print('Mamaco')
macaco1.comer('banana')
print(macaco1.verBucho())
macaco1.comer('uva')
print(macaco1.verBucho())
macaco1.comer('melancia')
print(macaco1.verBucho())
macaco1.digerir()
print(macaco1.verBucho())

print('\n Bill')
macaco2.comer('laranja')
print(macaco2.verBucho())
macaco2.comer('acerola')
print(macaco2.verBucho())
macaco2.comer('morango')
print(macaco2.verBucho())
macaco2.comer(macaco1)
print(macaco2.verBucho())