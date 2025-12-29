import csv
import os
import random

RUTINAS_DIR = "rutinas"
EJERCICIOS_CSV = "ejercicios.csv"

# Crear carpeta de rutinas si no existe
if not os.path.exists(RUTINAS_DIR):
    os.makedirs(RUTINAS_DIR)


def cargar_ejercicios():
    ejercicios = {}
    with open(EJERCICIOS_CSV, newline='', encoding="utf-8") as fichero:
        lector = csv.DictReader(fichero)
        for fila in lector:
            grupo = fila["grupo_muscular"]
            ejercicio = fila["ejercicio"]
            ejercicios.setdefault(grupo, []).append(ejercicio)
    return ejercicios


def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Introduce un número entre {minimo} y {maximo}")
        except ValueError:
            print("Entrada no válida")


def crear_rutina():
    ejercicios = cargar_ejercicios()

    dias = pedir_entero("¿Cuántos días entrenas a la semana? (3-5): ", 3, 5)
    tiempo = pedir_entero("¿Cuántos minutos por sesión? (45-90): ", 45, 90)

    grupos = list(ejercicios.keys())
    random.shuffle(grupos)

    rutina = {}
    for i in range(dias):
        # PEP 8: Espacios alrededor del operador +
        rutina[f"Día {i + 1}"] = []

    # Repartir grupos musculares asegurando que todos aparezcan
    for i, grupo in enumerate(grupos):
        dia = f"Día {(i % dias) + 1}"
        rutina[dia].append(grupo)

    resultado = f"Rutina de entrenamiento\nDías por semana: {dias}\nTiempo por sesión: {tiempo} minutos\n\n"

    for dia, grupos_dia in rutina.items():
        resultado += f"{dia}:\n"
        for grupo in grupos_dia:
            ejercicio = random.choice(ejercicios[grupo])
            resultado += f"  - {grupo.capitalize()}: {ejercicio}\n"
        resultado += "\n"

    print("\n--- RUTINA GENERADA ---\n")
    print(resultado)

    guardar = input("¿Deseas guardar la rutina? (s/n): ").lower()
    if guardar == "s":
        nombre = input("Nombre del archivo de la rutina: ")
        ruta = os.path.join(RUTINAS_DIR, nombre + ".txt")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(resultado)
        print("Rutina guardada correctamente.")


def cargar_rutina():
    archivos = os.listdir(RUTINAS_DIR)
    if not archivos:
        print("No hay rutinas guardadas.")
        return

    for i, archivo in enumerate(archivos, start=1):
        print(f"{i}. {archivo}")

    opcion = pedir_entero("Elige una rutina: ", 1, len(archivos))
    ruta = os.path.join(RUTINAS_DIR, archivos[opcion - 1])

    with open(ruta, encoding="utf-8") as f:
        print("\n--- RUTINA CARGADA ---\n")
        print(f.read())


def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear nueva rutina")
        print("2. Cargar rutina guardada")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_rutina()
        elif opcion == "2":
            cargar_rutina()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()

