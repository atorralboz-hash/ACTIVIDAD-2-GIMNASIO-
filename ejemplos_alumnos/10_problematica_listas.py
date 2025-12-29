# los datos de carla
nombre_carla = "carla"
edad_carla = "21"
altura = 1.82
dorsal = 12

""" transformación con listas """
jugadora_carla =["carla", "21", 1.82, "12"]
jugadora_lucia =["lucia", "22", 1.79, "10"]

print(jugadora_carla)

# acceder a un elemento
print(f"La edad de {jugadora_carla[0]} es {edad_carla[1]}")

# posicion de campo
jugadora_carla.append("Pivot")
print(jugadora_carla)

# eliminar edad de carla
jugadora_carla.remove("21")
print(jugadora_carla)

# eliminar las edades
jugadora_lucia.pop(1)
jugadora_carla.pop(1)
print(jugadora_carla)
print(jugadora_lucia)


