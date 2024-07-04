import os
import csv
import time
import random

comunas=["san Bernardo","Calera de Tango","Buin"]
sacos =(5,10,20)

with open ("datosdelpedido.csv","w") as pedidos:
    pedidosW = csv.writer(pedidos)




def reg_pedido():
    nro_pedido=random(1,100)
        