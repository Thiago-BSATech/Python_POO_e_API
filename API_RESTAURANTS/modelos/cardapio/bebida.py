from modelos.cardapio.itens_cardapio import Item_Cardapio

class Bebida(Item_Cardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} -- {self._tamanho} = {self._preco}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)