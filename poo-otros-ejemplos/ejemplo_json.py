import json

diccionario = {
   "estidiante1":{
       "Nombre": "Isaac Silva torrez",
       "genero": "Hombre",
   },
    "estudiante2":{
        "Nombre": "Jonathan Castro",
       "genero": "Hombre",
    }
}

print (diccionario["estudiante2"]["genero"])

diccionario1 = {
    "locura1":{
        "nombe": "jeois",
        "genero": "menestron"
    },
    "locura2":{
        "nombre": "elian",
        "genero": "lcour",
    }
}
print (diccionario1["locura1"]["genero"])

with open ("diccionario", "w") as archivo:
    json.dump (diccionario1, archivo)