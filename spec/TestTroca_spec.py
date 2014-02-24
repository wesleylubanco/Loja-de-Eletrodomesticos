#coding:utf-8
from should_dsl import should
import unittest
import specloud
from Cliente import *
from Produto import *
from Venda import *
from Troca import *

class TestTroca(unittest.TestCase):
    def TestaTroca(self):
        self.cliente = Cliente(1, "luiz", "rua a")
        self.venda = Venda(1,"10/11/2013", self.cliente)
        self.venda.data |should| equal_to ("10/11/2013")
        self.venda.cliente.id_cliente |should| equal_to (1)
        self.venda.cliente.nome |should| equal_to ("luiz")
        self.venda.cliente.endereco |should| equal_to ("rua a")
        self.produto = Produto(10, "marca a", "modelo a",321,30)
        self.venda.adicionar_produto(self.produto)
        self.venda.produtos[0].id_produto |should| equal_to (10)
        self.venda.produtos[0].marca |should| equal_to ("marca a")
        self.venda.produtos[0].modelo |should| equal_to ("modelo a")
        self.venda.produtos[0].numserie |should| equal_to (321)
	self.venda.produtos[0].quantidade |should| equal_to (30)
    
    def TestaGarantia(self):
	self.cliente = Cliente(1, "luiz", "rua a")
        self.vendaA = Venda(1,"01/10/2008",self.cliente)
        self.vendaA.data |should| equal_to ("01/10/2008")
        self.vendaA.tem_garantia() |should| equal_to (False)
        self.vendaB = Venda(1, "08/05/2013", self.cliente)
	self.vendaB.data |should| equal_to ("08/05/2013")
        self.vendaB.tem_garantia() |should| equal_to (True)
    
    def TestaAddTroca(self):
	self.cliente = Cliente(1, "luiz", "rua a")
	self.vendaA = Venda(1,"01/10/2008",self.cliente)
        self.troca = Troca("quebrado", "05/05/2013", self.vendaA, 100)
        self.troca.defeito |should| equal_to ("quebrado")
        self.troca.data |should| equal_to ("05/05/2013")
        self.troca.id_produto |should| equal_to (100)
        self.troca.quem_trocou() |should| equal_to ("luiz")
        pdef = Troca.listar_defeituosos()

    if __name__ == '__main__':
        unittest.main()
    

