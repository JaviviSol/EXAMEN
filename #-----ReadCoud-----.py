#-----ReadCloud-----
#............................

#---Menú---

def mostrar_menu():
    print()
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))

            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción entre el 1 y 6")

        except ValueError:
            print("Debe seleccionar una opción válida")


#---Validaciones---

def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    else:
        return True


def validar_precio_multa(precio_multa):
    if precio_multa > 0:
        return True
    else:
        return False


def validar_copias_disponibles(copias_disponibles):
    if copias_disponibles >= 0:
        return True
    else:
        return False


def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    else:
        return True


def validar_autor(autor):
    if autor.strip() == "":
        return False
    else:
        return True


def validar_genero(genero):
    if genero.strip() == "":
        return False
    else:
        return True


def validar_año(año):
    if año > 0:
        return True
    else:
        return False


def validar_editorial(editorial):
    if editorial.strip() == "":
        return False
    else:
        return True


def validar_es_novedad(es_novedad):
    es_novedad = es_novedad.strip().lower()

    if es_novedad == "s" or es_novedad == "n":
        return True
    else:
        return False


def validar_respuesta(respuesta):
    respuesta = respuesta.strip().lower()

    if respuesta == "s" or respuesta == "n":
        return True
    else:
        return False


#-----Funciones del sistema-----

#---Opción 1---

def copias_genero(genero, libros, prestamos):
    total_copias = 0
    genero = genero.strip().lower()

    for codigo in libros:
        genero_libro = libros[codigo][2].strip().lower()

        if genero_libro == genero:
            total_copias = total_copias + prestamos[codigo][1]

    print("El total de copias disponibles es:", total_copias)


#---Opción 2---

def busqueda_multa(multa_min, multa_max, libros, prestamos):
    libros_encontrados = []

    for codigo in prestamos:
        precio_multa = prestamos[codigo][0]
        copias_disponibles = prestamos[codigo][1]

        if precio_multa >= multa_min and precio_multa <= multa_max:
            if copias_disponibles != 0:
                titulo = libros[codigo][0]
                resultado = titulo + "--" + codigo
                libros_encontrados.append(resultado)

    libros_encontrados.sort()

    if len(libros_encontrados) > 0:
        print("Los libros encontrados son:", libros_encontrados)
    else:
        print("No hay libros en ese rango de multa.")


#---Opción 3---

def buscar_codigo(codigo, prestamos):
    codigo = codigo.strip().upper()
    codigo_encontrado = False

    for codigo_registrado in prestamos:
        if codigo_registrado.upper() == codigo:
            codigo_encontrado = True
            break

    return codigo_encontrado


def actualizar_multa(codigo, nueva_multa, prestamos):
    codigo = codigo.strip().upper()

    if buscar_codigo(codigo, prestamos) == True:
        prestamos[codigo][0] = nueva_multa
        return True
    else:
        return False


#---Opción 4---

def agregar_libro(codigo, titulo, autor, genero, año, editorial,
                  es_novedad, precio_multa, copias_disponibles,
                  libros, prestamos):

    codigo = codigo.strip().upper()

    if codigo in libros or buscar_codigo(codigo, prestamos) == True:
        return False
    else:
        libros[codigo] = [
            titulo.strip(),
            autor.strip(),
            genero.strip(),
            año,
            editorial.strip(),
            es_novedad
        ]

        prestamos[codigo] = [precio_multa, copias_disponibles]
        return True


#---Opción 5---

def eliminar_libro(codigo, libros, prestamos):
    codigo = codigo.strip().upper()

    if buscar_codigo(codigo, prestamos) == True:
        del libros[codigo]
        del prestamos[codigo]
        return True
    else:
        return False


#----------PROGRAMA PRINCIPAL----------

def programa_principal():

    #---Datos del sistema---

    libros = {
        'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
        'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
        'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
        'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
        'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
        'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
    }

    prestamos = {
        'L001': [500, 4],
        'L002': [700, 0],
        'L003': [300, 10],
        'L004': [400, 2],
        'L005': [600, 1],
        'L006': [350, 6]
    }

    opcion = 0

    while opcion != 6:

        mostrar_menu()
        opcion = leer_opcion()

        #---Opción 1---

        if opcion == 1:
            genero = input("Ingrese género a consultar: ")

            if validar_genero(genero) == True:
                copias_genero(genero, libros, prestamos)
            else:
                print("El género no puede estar vacío")

        #---Opción 2---

        elif opcion == 2:
            rango_valido = False

            while rango_valido == False:
                try:
                    multa_min = int(input("Ingrese multa mínima: "))
                    multa_max = int(input("Ingrese multa máxima: "))

                    if multa_min >= 0 and multa_max >= 0 and multa_min <= multa_max:
                        rango_valido = True
                    else:
                        print("El rango de multa no es válido")

                except ValueError:
                    print("Debe ingresar valores enteros")

            busqueda_multa(multa_min, multa_max, libros, prestamos)

        #---Opción 3---

        elif opcion == 3:
            seguir_actualizando = "s"

            while seguir_actualizando == "s":
                codigo = input("Ingrese código del libro: ")
                multa_valida = False

                while multa_valida == False:
                    try:
                        nueva_multa = int(input("Ingrese nueva multa: "))

                        if validar_precio_multa(nueva_multa) == True:
                            multa_valida = True
                        else:
                            print("La nueva multa debe ser mayor que cero")

                    except ValueError:
                        print("Debe ingresar un número entero")

                resultado_actualizacion = actualizar_multa(
                    codigo, nueva_multa, prestamos
                )

                if resultado_actualizacion == True:
                    print("Multa actualizada")
                else:
                    print("El código no existe")

                respuesta_valida = False

                while respuesta_valida == False:
                    seguir_actualizando = input(
                        "¿Desea actualizar otra multa (s/n)?: "
                    ).strip().lower()

                    if validar_respuesta(seguir_actualizando) == True:
                        respuesta_valida = True
                    else:
                        print("Debe ingresar s o n")

        #---Opción 4---

        elif opcion == 4:
            codigo = input("Ingrese código del libro: ")
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            genero = input("Ingrese género: ")

            try:
                año = int(input("Ingrese año de publicación: "))
            except ValueError:
                año = 0

            editorial = input("Ingrese editorial: ")
            es_novedad_ingresada = input("¿Es novedad? (s/n): ")

            try:
                precio_multa = int(input("Ingrese precio de multa: "))
            except ValueError:
                precio_multa = 0

            try:
                copias_disponibles = int(input("Ingrese copias disponibles: "))
            except ValueError:
                copias_disponibles = -1

            datos_validos = True

            if validar_codigo(codigo) == False:
                print("El código no puede estar vacío")
                datos_validos = False

            if validar_titulo(titulo) == False:
                print("El título no puede estar vacío")
                datos_validos = False

            if validar_autor(autor) == False:
                print("El autor no puede estar vacío")
                datos_validos = False

            if validar_genero(genero) == False:
                print("El género no puede estar vacío")
                datos_validos = False

            if validar_año(año) == False:
                print("El año debe ser un número entero mayor que cero")
                datos_validos = False

            if validar_editorial(editorial) == False:
                print("La editorial no puede estar vacía")
                datos_validos = False

            if validar_es_novedad(es_novedad_ingresada) == False:
                print("Debe ingresar s o n para indicar si es novedad")
                datos_validos = False

            if validar_precio_multa(precio_multa) == False:
                print("El precio de multa debe ser un número entero mayor que cero")
                datos_validos = False

            if validar_copias_disponibles(copias_disponibles) == False:
                print("Las copias disponibles deben ser un número entero mayor o igual a cero")
                datos_validos = False

            if datos_validos == True:
                if es_novedad_ingresada.strip().lower() == "s":
                    es_novedad = True
                else:
                    es_novedad = False

                resultado_agregar = agregar_libro(
                    codigo,
                    titulo,
                    autor,
                    genero,
                    año,
                    editorial,
                    es_novedad,
                    precio_multa,
                    copias_disponibles,
                    libros,
                    prestamos
                )

                if resultado_agregar == True:
                    print("Libro agregado")
                else:
                    print("El código ya existe")

        #---Opción 5---

        elif opcion == 5:
            codigo = input("Ingrese código del libro que desea eliminar: ")

            resultado_eliminar = eliminar_libro(
                codigo, libros, prestamos
            )

            if resultado_eliminar == True:
                print("Libro eliminado")
            else:
                print("El código no existe")

        #---Opción 6---

        elif opcion == 6:
            print("Programa finalizado.")


programa_principal()