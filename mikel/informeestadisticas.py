import sqlite3
from datetime import datetime

# ==================== CONFIGURACIÓN BASE DE DATOS ====================
def inicializar_bd():
    """Crea la base de datos y tablas si no existen"""
    conn = sqlite3.connect('autoplant.db')
    cursor = conn.cursor()
    
    # Tabla de inventario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pieza TEXT NOT NULL,
            stock INTEGER NOT NULL,
            minimo INTEGER NOT NULL,
            fecha_actualizacion TEXT
        )
    ''')
    
    # Tabla de producción histórica
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes TEXT NOT NULL,
            modelo TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            defectos INTEGER DEFAULT 0,
            fecha_registro TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def cargar_datos_ejemplo():
    """Carga datos de ejemplo si la BD está vacía"""
    conn = sqlite3.connect('autoplant.db')
    cursor = conn.cursor()
    
    # Verificar si ya hay datos
    cursor.execute('SELECT COUNT(*) FROM inventario')
    if cursor.fetchone()[0] == 0:
        # Datos de inventario
        inventario_inicial = [
            ('Motores', 450, 300),
            ('Transmisiones', 280, 250),
            ('Chasis', 520, 400),
            ('Paneles Negros', 180, 200),
            ('Paneles Blancos', 240, 200),
            ('Paneles Grises', 195, 150),
            ('Paneles Azules', 140, 120),
            ('Paneles Rojos', 110, 120),
        ]
        
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for pieza, stock, minimo in inventario_inicial:
            cursor.execute('''
                INSERT INTO inventario (pieza, stock, minimo, fecha_actualizacion)
                VALUES (?, ?, ?, ?)
            ''', (pieza, stock, minimo, fecha))
    
    # Verificar datos de producción
    cursor.execute('SELECT COUNT(*) FROM produccion')
    if cursor.fetchone()[0] == 0:
        # Datos de producción histórica
        produccion_inicial = [
            ('Enero', 'Sedán Sport', 245, 3),
            ('Enero', 'SUV Premium', 189, 2),
            ('Enero', 'Compacto City', 312, 4),
            ('Febrero', 'Sedán Sport', 260, 2),
            ('Febrero', 'SUV Premium', 195, 3),
            ('Febrero', 'Compacto City', 305, 5),
            ('Marzo', 'Sedán Sport', 250, 1),
            ('Marzo', 'SUV Premium', 200, 2),
            ('Marzo', 'Compacto City', 320, 3),
        ]
        
        fecha = datetime.now().strftime('%Y-%m-%d')
        for mes, modelo, cantidad, defectos in produccion_inicial:
            cursor.execute('''
                INSERT INTO produccion (mes, modelo, cantidad, defectos, fecha_registro)
                VALUES (?, ?, ?, ?, ?)
            ''', (mes, modelo, cantidad, defectos, fecha))
    
    conn.commit()
    conn.close()

# ==================== FUNCIONES DE INFORMES ====================

def mostrar_estadisticas():
    """Muestra estadísticas generales de producción"""
    conn = sqlite3.connect('autoplant.db')
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print(" ESTADÍSTICAS DE PRODUCCIÓN")
    print("="*60)
    
    # Total producido
    cursor.execute('SELECT SUM(cantidad) FROM produccion')
    total_producido = cursor.fetchone()[0] or 0
    
    # Total defectos
    cursor.execute('SELECT SUM(defectos) FROM produccion')
    total_defectos = cursor.fetchone()[0] or 0
    
    # Tasa de defectos
    tasa_defectos = (total_defectos / total_producido * 100) if total_producido > 0 else 0
    eficiencia = 100 - tasa_defectos
    
    print(f"\n   Producción Total:     {total_producido:,} unidades")
    print(f"    Defectos Totales:     {total_defectos} unidades")
    print(f"   Tasa de Defectos:     {tasa_defectos:.2f}%")
    print(f"   Eficiencia:           {eficiencia:.2f}%")
    
    # Producción por modelo
    print("\n" + "-"*60)
    print("Producción por Modelo:")
    print("-"*60)
    cursor.execute('''
        SELECT modelo, SUM(cantidad) as total, SUM(defectos) as defectos_total
        FROM produccion
        GROUP BY modelo
        ORDER BY total DESC
    ''')
    
    print(f"{'Modelo':<20} {'Producido':>12} {'Defectos':>12} {'Tasa':>10}")
    print("-"*60)
    for fila in cursor.fetchall():
        modelo, producido, defectos = fila
        tasa = (defectos / producido * 100) if producido > 0 else 0
        print(f"{modelo:<20} {producido:>12,} {defectos:>12} {tasa:>9.2f}%")
    
    conn.close()

def mostrar_historial_produccion():
    """Muestra el historial de producción mes a mes"""
    conn = sqlite3.connect('autoplant.db')
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print(" HISTORIAL DE PRODUCCIÓN")
    print("="*60)trh
    
    cursor.execute('''
        SELECT mes, SUM(cantidad) as total, SUM(defectos) as defectos_total
        FROM produccion
        GROUP BY mes
        ORDER BY id
    ''')
    
    print(f"\n{'Mes':<15} {'Producción':>15} {'Defectos':>12} {'Eficiencia':>12}")
    print("-"*60)
    
    for fila in cursor.fetchall():
        mes, produccion_mes, defectos = fila
        eficiencia = ((produccion_mes - defectos) / produccion_mes * 100) if produccion_mes > 0 else 0
        print(f"{mes:<15} {produccion_mes:>15,} {defectos:>12} {eficiencia:>11.2f}%")
    
    # Detalle por modelo y mes
    print("\n" + "="*60)

    print("Detalle por Modelo y Mes:")
    print("="*60)
    
    cursor.execute('''
        SELECT mes, modelo, cantidad, defectos
        FROM produccion
        ORDER BY mes, modelo
    ''')
    
    print(f"\n{'Mes':<12} {'Modelo':<20} {'Cantidad':>12} {'Defectos':>10}")
    print("-"*60)
    
    for fila in cursor.fetchall():
        mes, modelo, cantidad, defectos = fila
        print(f"{mes:<12} {modelo:<20} {cantidad:>12,} {defectos:>10}")
    
    conn.close()

def mostrar_informe_inventario():
    """Muestra el estado actual del inventario"""
    conn = sqlite3.connect('autoplant.db')
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print(" INFORME DE INVENTARIO")
    print("="*60)
    
    cursor.execute('SELECT pieza, stock, minimo, fecha_actualizacion FROM inventario')
    
    print(f"\n{'Pieza':<25} {'Stock':>10} {'Mínimo':>10} {'Estado':>15}")
    print("-"*60)
    
    alertas = []
    for fila in cursor.fetchall():
        pieza, stock, minimo, fecha = fila
        
        if stock < minimo:
            estado = " BAJO"
            alertas.append((pieza, stock, minimo))
        elif stock < minimo * 1.2:
            estado = " Próximo"
        else:
            estado = " Óptimo"
    
        print(f"{pieza:<25} {stock:>10,} {minimo:>10,} {estado:>15}")
    
    # Resumen de alertas
    if alertas:
        print("\n" + "="*60)
        print(" ALERTAS DE STOCK CRÍTICO")
        print("="*60)
        for pieza, stock, minimo in alertas:
            faltante = minimo - stock
            print(f"\n   {pieza}")
            print(f"     Stock actual: {stock} | Mínimo: {minimo} | Faltan: {faltante}")
    else:
        print("\n No hay alertas de stock crítico")
    
    conn.close()

# ==================== MENÚ PRINCIPAL ====================

def menu_principal():
    """Muestra el menú principal de informes"""
    while True:
        print("\n" + "="*60)
        print(" AUTOPLANT INDUSTRIES - SISTEMA DE INFORMES")
        print("="*60)
        print("\n1.  Ver Estadísticas de Producción")
        print("2.  Ver Historial de Producción")
        print("3.  Ver Informe de Inventario")
        print("4.  Ver Todos los Informes")
        print("5.  Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            mostrar_estadisticas()
        elif opcion == '2':
            mostrar_historial_produccion()
        elif opcion == '3':
            mostrar_informe_inventario()
        elif opcion == '4':
            mostrar_estadisticas()
            mostrar_historial_produccion()
            mostrar_informe_inventario()
        elif opcion == '5':
            print("\n👋 ¡Hasta luego!\n")
            break
        else:
            print("\n Opción no válida. Intente de nuevo.")
        
        input("\nPresione ENTER para continuar...")

# ==================== EJECUCIÓN ====================

if __name__ == "__main__":
    print("\n Inicializando sistema...")
    inicializar_bd()
    cargar_datos_ejemplo()
    print(" Sistema listo\n")
    menu_principal()