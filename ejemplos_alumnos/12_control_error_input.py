# pregunto al usuario si le gusta el zumo de naranja
respuesta = input ("te gusta el zumo de naranja [s|n]")

while respuesta.lower() != 's' and respuesta.lower () != 'n':
    respuesta = input("te gusta el zumo de naranja [s|n]")

if respuesta.lower() == 's':
   print("te gusta el zumo de naranja [s|n]")