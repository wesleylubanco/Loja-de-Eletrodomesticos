#coding:utf-8
from should_dsl import should
import unittest
import specloud
from Venda import *
from Cliente import *
from Produto import *

class TestVenda(unittest.TestCase):
     def TestaVenda(self):
        self.cliente = Cliente(1,"luiz","rua a")
        self.venda = Venda(10,"20/10/2013",self.cliente)
        self.venda.data |should| equal_to("20/10/2013")
        self.venda.cliente.id_cliente |should| equal_to (1)
        self.venda.cliente.nome |should| equal_to ("luiz")
        self.venda.cliente.endereco |should| equal_to ("rua a")
        
	self.produto = Produto(10,"marca a","modelo a",123,5)
        self.venda.adicionar_produto(self.produto)
        self.venda.produtos[0].id_produto |should| equal_to (10)
        self.venda.produtos[0].marca |should| equal_to ("marca a")
        self.venda.produtos[0].modelo |should| equal_to ("modelo a")
        self.venda.produtos[0].numserie |should| equal_to (123)
	self.venda.produtos[0].quantidade |should| equal_to (5)

     if __name__ == '__main__':
        unittest.main()
      
	
