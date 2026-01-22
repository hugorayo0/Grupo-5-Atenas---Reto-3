# Este python consiste en un mapa de la distribución de la fábrica de coches y proceso de producción de coches.

import os # Permite utilizar comandos del sistema como limpiar la pantalla, etc..
import json # Permite leer y escribir en archivos json

# Archivo en el que se guarda el estado de la producción del coche que produces.
ARCHIVO = "procesos.json"
# Funcion de ayuda que se explica que se hace en cada parte de la fábrica
def ayuda():
        while True:
                # Se pide al usuario que elija una opción del 1 al 5
                # Cada número corresponde a una parte del proceso de montaje de la fábrica
                NumOpcion = input("En que parte necesitas ayuda (1, 2, 3, 4 o 5) o 0 para salir: ")
                # Con el match y luego case para seleccionar la acción que debe de hacer en cada caso
                match NumOpcion:
                        case "0":
                                os.system("cls")
                                break
                        case "1": # Explica la parte de la carrocería
                                print("En esta primera parte, se fabrica y se ensambla la estructura principal del coche.")
                        case "2": # Explica la parte de las ruedas
                                print("En esta segunda parte, se instalan las ruedas para permitir el movimiento del coche.")
                        case "3": # Explica la parte de las ventanas
                                print("En esta tercera parte, se colocan los cristales y parabrisas para protección y visibilidad.")
                        case "4": # Explica la parte del motor
                                print("En esta cuarta parte, se monta el motor que proporcionará la potencia para el funcionamiento del coche.")
                        case "5": # Explica la parte de las luces
                                print("En esta ultima parte, se instalan los sistemas de iluminación y señalización.")
                        case _: # En el caso que no introduzca ninguna de las opciones validas
                                print("opcion no válida. Introduce un número del 1 al 5.")
def leerProcesos():
        # Lee el estado del coche del archivo procesos.json
        with open(ARCHIVO, "r") as f:
                global proceso
                proceso = json.load(f)
def GuardarProceso():
        # Guarda el estado del coche en el archivo procesos.json
        with open(ARCHIVO, "w") as f:
                json.dump(proceso, f, indent=4)
def carroceria():
        # Funcion de montaje de la carroceria y se comprueba que el montaje se realiza en el orden indicado en el mapa visual de la fábrica 
        if proceso['coches']['carroceria'] == 0:
                proceso['coches']['carroceria'] = 1
                print("Acabas de colocar la carroceria.")
                GuardarProceso()
        else:
                print("La carrocería ya estaba colocado.")
def ruedas():
        # Funcion de montaje de las ruedas y se comprueba que el montaje se realiza en el orden indicado en el mapa visual de la fábrica
        if proceso['coches']['ruedas'] == 0 and proceso['coches']['carroceria'] == 1:
                proceso['coches']['ruedas'] = 1
                print("Acabas de colocar las ruedas.")
                GuardarProceso()
        elif proceso['coches']['carroceria'] == 0:
                print("Debes colocar la carroceria antes que las ruedas.")
        else:
                print("Las ruedas ya estaban colocadas.")
def ventanas():
        # Funcion de montaje de las ventanas y se comprueba que el montaje se realiza en el orden indicado en el mapa visual de la fábrica
        if proceso['coches']['ventanas'] == 0 and proceso['coches']['ruedas'] == 1:
                proceso['coches']['ventanas'] = 1
                print("Acabas de colocar las ventanas.")
                GuardarProceso()
        elif proceso['coches']['ruedas'] == 0:
                print("Debes colocar las ruedas antes que las ventanas.")
        else:
                print("Las ventanas ya estaban colocadas.")
def motor():
        # Funcion de montaje del motor y se comprueba que el montaje se realiza en el orden indicado en el mapa visual de la fábrica
        if proceso['coches']['motor'] == 0 and proceso['coches']['ventanas'] == 1:
                proceso['coches']['motor'] = 1
                print("Acabas de colocar el motor.")
                GuardarProceso()
        elif proceso['coches']['ventanas'] == 0:
                print("Debes colocar las ventanas antes que el motor.")
        else:
                print("El motor ya estaba colocada.")
def luces():
        # Funcion de montaje de las luces y se comprueba que el montaje se realiza en el orden indicado en el mapa visual de la fábrica
        if proceso['coches']['luces'] == 0 and proceso['coches']['motor'] == 1:
                proceso['coches']['luces'] = 1
                print("Acabas de colocar las luces.")
                GuardarProceso()
        elif proceso['coches']['motor'] == 0:
                print("Debes colocar el motor antes que las luces.")
        else:
                print("Las luces ya estaban colocadas.")
def comprobacion():
        # Funcion para comprobar si se ha montado cada una de las partes correctamente.
        # En el caso que falten cosas muestra mensaje que faltan cosas por colocar.
        if proceso['coches']['carroceria'] == 1 and proceso['coches']['ruedas'] == 1 and proceso['coches']['ventanas'] == 1 and proceso['coches']['motor'] == 1 and proceso['coches']['luces'] == 1:
                print("Coche montado correctamente.")
        else:
                print("Faltan cosas por colocar.")
def ReiniciarProceso():
        # Reinicia el proceso para montar otro coche.
        proceso['coches']['carroceria'] = 0
        proceso['coches']['ruedas'] = 0
        proceso['coches']['ventanas'] = 0
        proceso['coches']['motor'] = 0
        proceso['coches']['luces'] = 0
        GuardarProceso()
def ProcesoProduccion():
        # Menu de opciones del proceso de producción
        while True:
                ParteProduccion = input("Que parte quieres montar(1, 2, 3, 4 o 5). 6 para comprobar. 7 para reiniciar el proceso. 0 para salir: ")
                match ParteProduccion:
                        case "0":
                                # Limpia la pantalla
                                os.system("cls")
                                break
                        case "1":
                                carroceria()
                        case "2":
                                ruedas()
                        case "3":
                                ventanas()
                        case "4":
                                motor()
                        case "5":
                                luces()
                        case "6":
                                comprobacion()
                        case "7":
                                ReiniciarProceso()
                        case _:
                                print("opción no válida")
# Menu principal del programa
while True:
        # Limpia la pantalla
        os.system("cls")
        # Mapa visual de la fábrica
        print("""         ______________________________________________
        |                                              |      
        |     ⬛⬛⬛⬛⬛⬛        1. CARROCERIA        |
        |               ⬛                             |
        |     ⬛⬛⬛⬛⬛⬛        2. RUEDAS            |
        |     ⬛                                       |
        |     ⬛⬛⬛⬛⬛⬛        3. VENTANAS          |
        |               ⬛                             |
        |     ⬛⬛⬛⬛⬛⬛        4. MOTOR             |
        |     ⬛                                       |
        |     ⬛⬛⬛⬛⬛⬛        5. LUCES             |
        |______________________________________________|
        """)
        opcion = input("Que quereis hacer? 0 para salir. 1 para ayuda del proceso de producción. 2 para realizar el proceso de producción: ")
        if opcion == "0":
                # Limpia la pantalla
                os.system("cls")
                break
        if opcion == "1":
                ayuda()
        elif opcion == "2":
                leerProcesos()
                ReiniciarProceso()
                ProcesoProduccion()
        else:
                print("Opción no válida")