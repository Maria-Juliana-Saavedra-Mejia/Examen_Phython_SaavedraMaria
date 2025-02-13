from modusuario import *

menu_principlal()
op=int(input("Digite su eleccion -> "))

if op==1:
    booleanito=True
    while booleanito==True:
        menu_clientes()
        c=int(input("Digite su eleccion -> "))
        if c==1:
            compra() 
        if c==2:
            info()
        if c== 3:
            consultas()
        if c== 4:
            booleanito=False

if op==2:
    booleanito=True
    while booleanito==True:
        menu_admin
        r=int(input("Digite su eleccion -> "))
        if r==1: 
            print("")
            
