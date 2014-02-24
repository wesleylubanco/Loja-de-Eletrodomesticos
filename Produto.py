#coding:utf-8
class Produto:
    produtos = []
    def __init__(self,id_produto,marca,modelo,numserie,quantidade):
        self.id_produto = id_produto
        self.marca = marca
        self.modelo = modelo
        self.numserie = numserie
        self.quantidade = quantidade
    
    @staticmethod
    def adicionar_produto(self):
         Produto.produtos.append(self)
    
    @staticmethod
    def remover(self):
        Produto.produtos.remove(self)
    
    @staticmethod
    def alterar_produto(self):
        for i in range (0, len(produto.produtos)):
            if Produto.produtos[i].id_produto == self.id_produto:
                Produto.produtos[i] = self
    
    @staticmethod    
    def adicionar_estoque (self,quantidade):
        self.quantidade += quantidade
        Produto.alterar_produto(self)

    @staticmethod
    def remover_estoque (self,quantidade):
        self.quantidade -= quantidade
        Produto.alterar_produto(self)

    @staticmethod
    def disponiveis():
        disponiveis = []
        for i in range (0, len(Produto.produtos)):
            if Produto.produtos[i].quantidade > 0:
                p = Produto(Produto.produtos[i].id_produto,Produto.produtos[i].marca,Produto.produtos[i].modelo,Produto.produtos[i].numserie, Produto.produtos[i].quantidade)
                disponiveis.append(p)
        return disponiveis

    @staticmethod
    def buscar(id_produto):
        for i in range (0, len(Produto.produtos)):
            if Produto.produtos[i].id_produto == id_produto:
                p = Produto(Produto.produtos[i].id_produto,Produto.produtos[i].marca,Produto.produtos[i].modelo,Produto.produtos[i].numserie, Produto.produtos[i].quantidade)
                return p
