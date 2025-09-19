from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco de laranja', 7.50 , 300)
prato_bife = Prato('bife acebolado', 29.90, 'Bife com cebolas douradas na manteiga')
restaurante_praca.adicionar_no_cardapio(prato_bife)
restaurante_praca.adicionar_no_cardapio(bebida_suco)



def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()