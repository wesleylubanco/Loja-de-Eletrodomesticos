from should_dsl import should
import unittest
import specloud
from Cliente import *

class TestCliente(unittest.TestCase):
     
     def TestaNovoCliente(self):
        self.cliente = Cliente(1,"Luiz","rua a")
        self.cliente.id_cliente |should| equal_to(1)
        self.cliente.nome |should| equal_to("Luiz")
        self.cliente.endereco |should| equal_to("rua a")

     def TestaCadastrarCliente(self):
	self.cliente = Cliente(1,"Luiz","rua a")	
	Cliente.add_cliente(self.cliente)
	Cliente.clientes[0].id_cliente |should| equal_to(1)
	Cliente.clientes[0].nome |should| equal_to("Luiz")
	Cliente.clientes[0].endereco |should| equal_to("rua a")

     def TestaBuscaCliente(self):
	self.cliente = Cliente(1,"Luiz","rua a")	
	Cliente.add_cliente(self.cliente)
	c = Cliente.buscar(self,1)	
     	c.nome |should| equal_to("Luiz")
	c.endereco |should| equal_to("rua a")

     if __name__ == '__main__':
        unittest.main()
	
	
 
