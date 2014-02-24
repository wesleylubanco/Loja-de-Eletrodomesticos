#coding:utf-8
from should_dsl import should
import unittest
import specloud
from Produto import *

class TestProduto(unittest.TestCase):
 
    def TestaCadastrarProduto(self):
        self.produto = Produto(1,"marca a","modelo b",653,30)
        self.produto.id_produto |should| equal_to (1)
        self.produto.marca |should| equal_to ("marca a")
        self.produto.modelo |should| equal_to ("modelo b")
        self.produto.numserie |should| equal_to (653)
	self.produto.quantidade |should| equal_to (30)
        Produto.adicionar_produto(self.produto)

    def TestaListarDisponiveis(self):
        produto = Produto.disponiveis()
        produto[0].id_produto |should| equal_to(1)
	produto[0].marca |should| equal_to ("marca a")
	produto[0].modelo |should| equal_to("modelo b")        
	produto[0].numserie |should| equal_to(653)	
	produto[0].quantidade |should| equal_to(30)

    def TestaRemoverProduto(self):
        self.produto = Produto(1,"marca a","modelo b",653,30)
	Produto.adicionar_produto(self.produto)        
	Produto.remover(self.produto)
     
    if __name__ == '__main__':
        unittest.main()
	
	
 
