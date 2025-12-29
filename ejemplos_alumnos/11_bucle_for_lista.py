# lista de nomnbres
lista_nombres = ["alejandra", "poncho", "gigi", "michu"]

# recorrer la lista con un for
for nombre in lista_nombres:
    print(nombre.upper())

# con upper() pone los nombres en mayuscula
# lista de numeros
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista_numeros:
    if numero < 10:
        print(numero)

# temperaturas de un sensor de un congelador
temperaturas_sensor = [-5, -6, -5, -8, 0, -4 ,-5]
for temperatura in temperaturas_sensor:
    if temperatura >=0:
        print(f"{temperatura} es mayor o igual a {0}")
        print("Existe un error en el congelador")
        break
    print(f"La temperatura es {temperatura}")