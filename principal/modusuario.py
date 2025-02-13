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
    for i in range (len(planes)):
        print(i+1, " : ", planes[i]) 
        



def info():
    id=int(input("Digite su numero de identidad -> "))
    ids=abrirJSONusuarios
    print(["Nombre"])

def consultas():
    print(" ")

def menu_admin():
    print("Agregar o eliminar un servicio (1)")
    print ("Reportes (2)")
    print("Modulo clientes leales (3)")
    print("Salir (4)")




    
