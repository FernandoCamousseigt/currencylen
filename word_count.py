import sys

archivo = sys.argv[1]

with open(archivo, "r") as file:  #as file or as thenameyouwant
    texto = file.read()

#print(texto)
#run terminal: python word_count.py lorem_ipsum.txt

caracteres = set(texto)
cuenta_car = len(caracteres)

print("El número de caracteres distintos es:", cuenta_car)

palabras = texto.split(" ")

cuenta_pal = len(set(palabras))

print("El número de palabras distintas es:", cuenta_pal)

#run terminal: python word_count.py lorem_ipsum.txt

