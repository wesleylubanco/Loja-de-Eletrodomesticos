#coding:utf-8
from datetime import date
class Venda:
  vendas = []
  def __init__(self,id_venda,data,cliente):
    self.id_venda = id_venda
    self.data = data
    self.cliente = cliente
    self.produtos = []

  def adicionar_produto(self,produto):
    self.produtos.append(produto)

  @staticmethod
  def guardar_vendas(self):
    Venda.vendas.append(self)

  @staticmethod
  def buscar_vendas(self,id_venda):
    for i in range (0,len(Venda.vendas)):
      if Venda.vendas[i].id_venda == id_venda:
        return Venda.vendas[i]
  
  def tem_garantia(self):
    data = date.today()
    datav = date(int(self.data[6:10]), int(self.data[3:5]), int(self.data[0:2]))
    ano = datav.year+1
    garantia= date(ano,datav.month,datav.day)
    if data <= garantia:
      return True
    else:
      return False
