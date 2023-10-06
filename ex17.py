'''Crie uma Fazenda de Bichinhos instanciando vários objetos 
bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de 
exigir que o usuário tome conta de um único bichinho, 
exija que ele tome conta da fazenda inteira. Cada opção 
do menu deveria permitir que o usuário executasse uma ação 
para todos os bichinhos (alimentar todos os bichinhos, brincar 
com todos os bichinhos, ou ouvir a todos os bichinhos). Para 
tornar o programa mais interessante, dê para cada bichinho 
um nivel inicial aleatório de fome e tédio. '''

class BichinhoVirtual:
    def __init__(self, nome, fome, humor):
        self.nome = nome
        self.fome = fome
        self.saude = 100
        self.idade = 0
        self.humor = humor

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

bichinho1 = BichinhoVirtual('Lontra', 40, 80)
bichinho2 = BichinhoVirtual('Margarida', 50, 36)
bichinho3 = BichinhoVirtual('Pato', 90, 90)
bichinhos = [bichinho1, bichinho2, bichinho3]

while True:
    print('Escolha entre as opções:')
    print('1. Alimentar todos os bichinhos')
    print('2. Brincar com todos os bichinhos')
    print('3. Ouvir todos os bichinhos')
    print('4. Sair')
    opcao = input('Digite sua resposta: ')

    if opcao == '1':
        comida = int(input('Digite a quantidade de comida: '))
        for bichinho in bichinhos:
            bichinho.alimentar(comida)

    elif opcao == '2':
        brincando = float(input('Digite o tempo brincando: '))
        for bichinho in bichinhos:
            bichinho.brincar(brincando)

    elif opcao == '3':
        for bichinho in bichinhos:
            bichinho.str()

    else:
        break