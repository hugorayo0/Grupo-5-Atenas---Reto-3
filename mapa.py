# Este python consiste en un mapa de la distribución de la fábrica de coches.
import os
os.system("cls")
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
# Se pide al usuario que elija una opción del 1 al 5
# Cada número corresponde a una parte del proceso de montaje de la fábrica
while True:
        NumOpcion = input("Que parte quieres (1, 2, 3, 4 o 5) o 0 para salir: ")
        # Con el match y luego case para seleccionar la acción que debe de hacer en cada caso
        match NumOpcion:
                case "0":
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