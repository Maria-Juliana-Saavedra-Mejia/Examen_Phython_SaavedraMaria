from modusuario import *

menu_principlal()
op=int(input("Digite su eleccion -> "))

if op==1:
    menu_clientes()
    c=int(input("Digite su eleccion -> "))
    if c==1:
       compra() 
