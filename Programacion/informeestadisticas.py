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
