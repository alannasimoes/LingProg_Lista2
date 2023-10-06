'''Classe TV: Faça um programa que simule um televisor 
criando-o como um objeto. O usuário deve ser capaz de 
informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume 
permanecem dentro de faixas válidas. '''

class Televisor:
    def __init__(self, volume=20, canal=1):
        self.volume = volume
        self.canal = canal

    def alterarVolume(self, volume_novo):
        if volume_novo > 100 or volume_novo < 0:
            print('Volume inválido')
        else:
            self.volume = volume_novo

    def mudarCanal(self, canal_novo):
        if canal_novo > 20 or canal_novo < 1:
            print('Canal inválido')
        else:
            self.canal = canal_novo
