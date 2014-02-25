#coding:utf-8
class Troca:
    trocas = []
    def __init__(self,defeito,data,venda,id_produto):
        self.defeito = defeito
        self.data = data
        self.venda = venda
        self.id_produto = id_produto
    
    def troca(self):
        if self.venda.tem_garantia:
            self.trocas.append(self)

    def quem_trocou(self):
        return self.venda.cliente.nome

    @staticmethod
    def listar_defeituosos():
        return Troca.trocas
