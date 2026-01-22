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

while True:
    print("1) Ver inventario")
    print("2) Estadisticas")
    print("3) Distribucion de la fabrica")
    print("4) Salir")
    Opcion = int(input("Seleccione el apartado que quiera ver por numero: "))
    match Opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            print("Cerrando sesión")
            break
        case _:
            print("No es una opcion en la lista")
