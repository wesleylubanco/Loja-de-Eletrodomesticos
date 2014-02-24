#coding:utf-8
class Cliente:
    clientes = []
    def __init__(self,id_cliente,nome,endereco):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco

    @staticmethod
    def add_cliente(cliente):
         Cliente.clientes.append(cliente)
         
    @staticmethod
    def buscar(self,id_cliente):
        for i in range (0, len(Cliente.clientes)):
            if Cliente.clientes[i].id_cliente == id_cliente:
                c = Cliente(Cliente.clientes[i].id_cliente, Cliente.clientes[i].nome, Cliente.clientes[i].endereco)
                return c 
