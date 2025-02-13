import json
def abrirJSONconsultas():
    dicFinal={}
    with open("../jsons/consultas.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSONconsultas(dic):
    with open("../jsons/consultas.json",'w') as outFile:
        json.dump(dic,outFile)



def abrirJSONusuarios():
    dicFinal={}
    with open("../jsons/usuarios.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSONusuarios(dic):
    with open("../jsons/usuarios.json",'w') as outFile:
        json.dump(dic,outFile)



def abrirJSONcostoPlanes():
    dicFinal={}
    with open("../jsons/costoPlanes",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSONcostoPlanes(dic):
    with open("../jsons/costoPlanes",'w') as outFile:
        json.dump(dic,outFile)



def abrirJSONplanes():
    dicFinal={}
    with open("../jsons/planes.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSONplanes(dic):
    with open("../jsons/planes.json",'w') as outFile:
        json.dump(dic,outFile)
