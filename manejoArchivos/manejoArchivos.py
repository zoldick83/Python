import csv
"""
with open('config.txt','r')as archivo:
    lineas = archivo.readlines()
    print(lineas)
"""
with open('personas.csv') as archivo:
    lectura = csv.reader(archivo)
    for fila in lectura:
        print("Ap Paterno:{0},Nombre:{1},Edad:{2}".format(fila[0],fila[1],fila[2]))
