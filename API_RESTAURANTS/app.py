from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_1 = Restaurante('Pizzaria do Zé', 'Italiana')


restaurante_1.add_ao_cardapio(Bebida('Refrigerante', 8.00, 'coquinha'))
restaurante_1.add_ao_cardapio(Prato('Pizza de Calabresa', 20.00, "descricao 123"))


def main():
    restaurante_1.exibir_cardapio

if __name__ == '__main__':
    main()