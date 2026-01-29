import json
import os

ARCHIVO = "piezas.json"

def cargar():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump({}, f)
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar(piezas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(piezas, f, indent=4, ensure_ascii=False)

while True:
    piezas = cargar()

    print("\n1 ver | 2 añadir | 3 eliminar | 4 salir")
    opcion = input("> ")

    if opcion == "1":
        for p, c in piezas.items():
            print(p, ":", c)

    elif opcion == "2":
        p = input("pieza: ")
        c = int(input("cantidad: "))
        piezas[p] = piezas.get(p, 0) + c
        guardar(piezas)

    elif opcion == "3":
        p = input("pieza: ")
        if p in piezas:
            del piezas[p]
            guardar(piezas)

    elif opcion == "4":
        print("Saliendo...")
        break
