'''Classe Bomba de Combustível: Faça um programa completo 
utilizando classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo 
    esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel 
    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor 
        a ser abastecido e mostra a quantidade de litros que 
        foi colocada no veículo
        abastecerPorLitro( ) – método onde é informado a 
        quantidade em litros de combustível e mostra o valor 
        a ser pago pelo cliente.
        alterarValor( ) – altera o valor do litro do combustível.
        alterarCombustivel( ) – altera o tipo do combustível.
        alterarQuantidadeCombustivel( ) – altera a quantidade de 
        combustível restante na bomba. 
    OBS: Sempre que acontecer um abastecimento é necessário atualizar 
    a quantidade de combustível total na bomba.'''

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecePorValor(self, valor):
        litros = valor/self.valor_litro
        self.quantidade_combustivel -= litros
        print(f'Foram abastecidos {litros}L')

    def abastecerPorLitro(self, litros):
        preco = litros*self.valor_litro
        self.quantidade_combustivel -= litros
        print(f'O valor foi R${preco}')

    def alterarValor(self, valor_novo):
        self.valor_litro = valor_novo

    def alterarQuantidadeCombustivel(self, quantidade_nova):
        self.quantidade_combustivel = quantidade_nova