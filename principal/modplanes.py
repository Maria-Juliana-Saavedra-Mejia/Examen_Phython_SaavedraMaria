def menu_admin():
    print("Agregar, eliminar o editar un servicio (1)")
    print ("Reportes (2)")
    print("Modulo clientes leales (3)")
    print("Salir (4)")

def aged():
    print("Eliminar (1)")
    print("Agregar (2)")
    print("Editar (3)")
    print("Salir (4)")
    op=int(input("Digite su eleccion -> "))
    if op== 1:
        planes={}
        planes=abrirJSONplanes()
        costo={}
        costo=abrirJSONcostoPlanes()
        for i in range (len(planes)):
            print(i+1, " : ", planes[i], " $ ", costo[i])
            e=int(input("Digite el numero del servicio que quiere eliminar-> "))

        guardarJSONplanes
        guardarJSONcostoPlanes