'''Crie uma "porta escondida" no programa do 
programa do bichinho virtual que mostre os 
valores exatos dos atributos do objeto. Consiga 
isto mostrando o objeto quando uma opção secreta, 
não listada no menu, for informada na escolha do 
usuário. Dica: acrescente um método especial str() 
à classe Bichinho. '''

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.saude = 100
        self.idade = 0
        self.humor = 100

    def alterarNome(self, nome_novo):
        self.nome = nome_novo

    def alterarFome(self, fome_nova):
        if fome_nova > 100 or fome_nova < 0:
            print('Valor inválido')
        else:
            self.fome = fome_nova

    def alterarSaude(self, saude_nova):
        if saude_nova > 100 or saude_nova < 0:
            print('Valor inválido')
        else:
            self.saude = saude_nova

    def alterarIdade(self, idade_nova):
        if idade_nova < 0:
            print('Valor inválido')
        else:
            self.idade = idade_nova

    def retornaNome(self):
        return self.nome
    
    def retornaFome(self):
        return self.fome
    
    def retornaSaude(self):
        return self.saude
    
    def retornaIdade(self):
        return self.idade
    
    def humor(self):
        valor_humor = self.fome + self.saude
        if valor_humor > 150:
            return 'Feliz'
        elif valor_humor > 100:
            return 'Normal'
        elif valor_humor > 50:
            return 'Triste'
        else:
            return 'Morrendo'
        self.humor = valor_humor/2
        
    def alimentar(self, quantidade_comida):
        if quantidade_comida > 5:
            self.fome = 100
        elif quantidade_comida > 3:
            if self.fome > 40:
                self.fome = 100
            else:
                self.fome += 60
        else:
            if self.fome > 80:
                self.fome = 100
            else:
                self.fome += 20

    def brincar(self, tempo_brincando):
        if tempo_brincando > 5:
            self.humor = 100
        elif tempo_brincando > 3:
            if self.humor > 40:
                self.humor = 100
            else:
                self.humor += 60
        else:
            if self.humor > 80:
                self.humor = 100
            else:
                self.humor += 20

    def str(self):
        print(f'Nome: {self.nome}')
        print(f'Fome: {self.fome}')
        print(f'Saúde: {self.saude}')
        print(f'Idade: {self.idade}')
        print(f'Humor: {self.humor}')
