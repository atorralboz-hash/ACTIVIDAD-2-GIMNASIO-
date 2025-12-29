# Semaforo
# verde = 1
# amarillo = 2
# rojo 3
verde = 1
amarillo = 2
rojo = 3

# Estado del semaforo
semaforo = rojo

# Control del trafico
if semaforo == verde:
    print("Esta en verde")
    print("Puedes pasar")
elif semaforo == amarillo:
    print("Esta en amarillo")
    print("Puedes pasar corriendo")
elif semaforo == rojo:
    print("Esta en rojo")
    print("No puedes pasar")
else:
    print("El semaforo está roto")

print("CONTINUA DESPUES DEL IF")