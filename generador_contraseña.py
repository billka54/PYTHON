import random

minuscula = "abcdefghijklmnopqrstuvwxyz"
mayuscula = minuscula.upper()
numeros = "0123456789"
simobolos = "$#&/()=?¿!"

base = minuscula + mayuscula + numeros + simobolos
longitud = 16

for _ in range(100):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    print (password)