from jsonmod import*

def menu_principlal():
    print("Bienvenido a Movistar")
    print("Cliente (1)")
    print("Administrador (2)")

def menu_clientes():
    print("Para realizar una compra (1)")
    print("Para revisar su informaciòn personal (2)")
    print("Consultas (3)")
    print("Salir (4)")

def compra():
    print("Estos son los planes disponibles: ")
    planes={}
    planes=abrirJSONplanes()
    costo={}
    costo=abrirJSONcostoPlanes()
    for i in range (len(planes)):
        print(i+1, " : ", planes[i], " $ ", costo[i])
    e=int(input("Digite el numero del servicio que quiere obtener -> "))
    id=int(input("Digite su ID-> "))
    nom=input("Digite su nombre-> ")
    dir=input("Digite su Direccion-> ")
    num=int(input("Digite su Numero de telefonop> "))
    categoria =""
    clientenuevo={}
    clientenuevo["Nombre"]=nom
    clientenuevo["Nombre"]=nom
    clientenuevo["Nombre"]=nom
    clientenuevo["Nombre"]=nom
    

    guardarJSONusuarios


    

def info():
    id=int(input("Digite su numero de identidad -> "))
    ids={}
    ids=abrirJSONusuarios()
    for i in range (len(ids)):
        if id==ids["ID"][i]:
            print("Bienvenido Usuario: ")
            print("Nombre: ", ids["Nombre"])
            print("Direccion: ", ids["Direccion"])
            print("Numero de telefono: ", ids["Numero de telefono"])
            print("Plan: ", ids["Plan"])
            print("Categoria: ", ids["Categoria"])

def consultas():
    print(" ")







    
