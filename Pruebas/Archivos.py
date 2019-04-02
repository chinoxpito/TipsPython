#ARCHIVOS
#MANEJO DE LECTURA Y ESCRITURA DE ARCHIVOS

a=open("C:\Git\TipsPython\Pruebas\Doc\ANEXOS.txt", "r") # w :write - r: read

#leer  = a.read() #LEE TODO EL ARCHIVO

leer  = a.readline()
print(leer)
leer2  = a.readline()
print(leer2)

#ESCRITURA

b = open("C:\Git\TipsPython\Pruebas\Doc\ArchivoEscritura.txt", "w") #esto abre el archivo y remplaza todo lo que hay dentro

b.write("Uno \nDos \nTres")

b.close()

