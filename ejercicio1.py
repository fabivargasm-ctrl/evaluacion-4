libros = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar un número entre 1 y 6.")
        except ValueError:
            print("Debe ingresar un número válido.")

def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True


def validar_copias(copias):
    if copias >= 0:
        return True
    return False


def validar_prestamo(prestamo):
    if prestamo > 0:
        return True
    return False

def agregar_libro(libros):
    titulo = input("Ingrese el título del libro: ")

    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío.")
        return

    try:
        copias = int(input("Ingrese la cantidad de copias: "))
    except ValueError:
        print("Error: las copias deben ser un número entero.")
        return

    if not validar_copias(copias):
        print("Error: las copias deben ser mayor o igual a 0.")
        return

    try:
        prestamo = int(input("Ingrese el período de préstamo: "))
    except ValueError:
        print("Error: el período debe ser un número entero.")
        return

    if not validar_prestamo(prestamo):
        print("Error: el período debe ser mayor que 0.")
        return

    libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": False
    }

    libros.append(libro)
    print("Libro agregado correctamente.")

def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"] == titulo:
            return i
    return -1

def eliminar_libro(libros):
    titulo = input("Ingrese el título del libro a eliminar: ")

    posicion = buscar_libro(libros, titulo)

    if posicion != -1:
        libros.pop(posicion)
        print("Libro eliminado correctamente.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

def mostrar_libros(libros):
    actualizar_disponibilidad(libros)

    print("=== LISTA DE LIBROS ===")

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    for libro in libros:
        print("Título:", libro["titulo"])
        print("Copias:", libro["copias"])
        print("Préstamo:", libro["prestamo"])

        if libro["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN COPIAS")

        print("*********************************************")

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        titulo = input("Ingrese el título del libro a buscar: ")
        posicion = buscar_libro(libros, titulo)

        if posicion != -1:
            print("Libro encontrado:")
            print("Título:", libros[posicion]["titulo"])
            print("Copias:", libros[posicion]["copias"])
            print("Préstamo:", libros[posicion]["prestamo"])
            print("Disponible:", libros[posicion]["disponible"])
        else:
            print("Libro no encontrado.")

    elif opcion == 3:
        eliminar_libro(libros)

    elif opcion == 4:
        actualizar_disponibilidad(libros)
        print("Disponibilidad actualizada.")

    elif opcion == 5:
        mostrar_libros(libros)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break
