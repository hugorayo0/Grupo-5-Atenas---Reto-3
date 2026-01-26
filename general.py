Usuario = 'Admin'
Password = '1234'

ALogin = False

u = input ('Introdir nombre de usuario: ')
p = input ('Introduce tu contraseña: ')

if u == Usuario and p == Password:
    ALogin = True
    print('Has iniciado sesion como Admin')

else:
    print("Acceso denegado ")

if ALogin:
    while True:
        print("1) Ver inventario")
        print("2) Estadisticas")
        print("3) Distribucion de la fabrica")
        print("4) Salir")
        Opcion = int(input("Seleccione el apartado que quiera ver por numero: "))
        match Opcion:
            case 1:
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
            case 2:
                import sqlite3
                
                # Crear base de datos
                def crear_bd():
                    conn = sqlite3.connect('autoplant.db')
                    c = conn.cursor()
                    
                    c.execute('''CREATE TABLE IF NOT EXISTS inventario (
                        pieza TEXT, stock INTEGER, minimo INTEGER)''')
                    
                    c.execute('''CREATE TABLE IF NOT EXISTS produccion (
                        mes TEXT, modelo TEXT, cantidad INTEGER, defectos INTEGER)''')
                    
                    conn.commit()
                    conn.close()
                
                # Agregar datos ejemplo
                def datos_ejemplo():
                    conn = sqlite3.connect('autoplant.db')
                    c = conn.cursor()
                    
                    c.execute('SELECT COUNT(*) FROM inventario')
                    if c.fetchone()[0] == 0:
                        piezas = [
                            ('Motores', 450, 300),
                            ('Transmisiones', 280, 250),
                            ('Chasis', 520, 400),
                            ('Paneles Negros', 180, 200)
                        ]
                        c.executemany('INSERT INTO inventario VALUES (?,?,?)', piezas)
                        
                        produccion = [
                            ('Enero', 'Sedán Sport', 245, 3),
                            ('Enero', 'SUV Premium', 189, 2),
                            ('Febrero', 'Sedán Sport', 260, 2)
                        ]
                        c.executemany('INSERT INTO produccion VALUES (?,?,?,?)', produccion)
                    
                    conn.commit()
                    conn.close()
                
                # Ver estadísticas
                def estadisticas():
                    conn = sqlite3.connect('autoplant.db')
                    c = conn.cursor()
                    
                    print("\n=== ESTADÍSTICAS ===")
                    c.execute('SELECT SUM(cantidad), SUM(defectos) FROM produccion')
                    total, defectos = c.fetchone()
                    
                    print(f"Producido: {total} unidades")
                    print(f"Defectos: {defectos}")
                    print(f"Eficiencia: {100 - (defectos/total*100):.1f}%")
                    
                    conn.close()
                
                # Ver producción
                def produccion():
                    conn = sqlite3.connect('autoplant.db')
                    c = conn.cursor()
                    
                    print("\n=== PRODUCCIÓN ===")
                    c.execute('SELECT * FROM produccion')
                    
                    for mes, modelo, cant, def_ in c.fetchall():
                        print(f"{mes} - {modelo}: {cant} ({def_} defectos)")
                    
                    conn.close()
                
                # Ver inventario
                def inventario():
                    conn = sqlite3.connect('autoplant.db')
                    c = conn.cursor()
                    
                    print("\n=== INVENTARIO ===")
                    c.execute('SELECT * FROM inventario')
                    
                    for pieza, stock, minimo in c.fetchall():
                        estado = "BAJO" if stock < minimo else "OK"
                        print(f"{pieza}: {stock} (mín: {minimo}) - {estado}")
                    
                    conn.close()
                
                # Menú
                def menu():
                    while True:
                        print("\n=== AUTOPLANT ===")
                        print("1. Estadísticas")
                        print("2. Producción")
                        print("3. Inventario")
                        print("4. Salir")
                        
                        op = input("\nOpción: ")
                        
                        if op == '1':
                            estadisticas()
                        elif op == '2':
                            produccion()
                        elif op == '3':
                            inventario()
                        elif op == '4':
                            break
                        
                        input("\nENTER para continuar...")
                
                # Iniciar
                crear_bd()
                datos_ejemplo()
                menu()
            case 3:
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
            case 4:
                print("Cerrando sesión")
                break
            case _:

                print("No es una opcion en la lista")

