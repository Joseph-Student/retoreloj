import locale

from reloj import Reloj

locale.setlocale(locale.LC_ALL, '')


def menu():
    print("Estas son las oparaciones que se pueden realizar: ")
    print("1- Ver la hora en Greenwich.")
    print("2- Ver la fecha y la hora en Greenwich.")
    print("3- Ver la fecha y la hora en Nueva York.")
    print("4- Ver la fecha y la hora en Los Angeles.")
    print("5- Ver la fecha y la hora en Venezuela.")
    print("6- Ver la fecha y la hora en Holanda.")
    print("7- Mostrar el menu nuevamente.")
    print("8- Salir")


def mostrar_reloj():
    print("Bienvenido al reloj mundial hecho por Joseph Perez.\n")
    menu()
    while True:
        lugar = 'Greenwich'
        zona_horaria = 0
        mostrar = 'fecha y la hora'
        try:
            resp = int(input("Escriba su opcion: "))
            print()
        except ValueError:
            print("Por favor introduzca un numero.")
            mostrar_reloj()
        else:
            if resp is 1:
                mostrar = 'hora'
            elif resp is 2:
                pass
            elif resp is 3:
                zona_horaria = -4
                lugar = "Nueva York"
            elif resp is 4:
                zona_horaria = -7
                lugar = "Los Angeles"
            elif resp is 5:
                zona_horaria = -4.5
                lugar = "Venezuela"
            elif resp is 6:
                zona_horaria = 2
                lugar = "Holanda"
            elif resp is 7:
                menu()
                continue
            elif resp is 8:
                break
            else:
                print("Esta opcion no se encuentra disponible")

            reloj = Reloj(zona_horaria=zona_horaria, lugar=lugar)
            if mostrar is 'hora':
                resultado = reloj.get_hora_formato()
            else:
                resultado = str(reloj)
            mensaje = "La {} en {} con zona horaria de {} es: {}".format(
                mostrar,
                lugar,
                zona_horaria,
                resultado
            )
            print(mensaje)
            print()


if __name__ == '__main__':
    mostrar_reloj()
    print()
    print("Gracias por usar el reloj del mundo")
