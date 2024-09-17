import random

colores = ['amarillo', 'azul', 'verde', 'rojo']
usuarios = [{'Nombre': 'Josep'}, {'Nombre': 'Claudio'}, {'Nombre': 'Isabel'}, {'Nombre': 'Sheila'}]


def agregar_color():
    while True:
        color = input("Ingresa un nuevo color: ").lower()
        if color not in colores:
            colores.append(color)
            print(f"Color {color} añadido exitosamente!")
            break
        else:
            print(f"Color {color} ya existe en la lista.")


def asignar_colores():
    if len(colores) < len(usuarios):
        print("No hay suficientes colores para asignar a todos los usuarios.")
        return
    random.shuffle(colores)
    for usuario, color in zip(usuarios, colores):
        usuario['Color'] = color
    print("Colores asignados exitosamente!")


def mostrar_colores():
    for color in sorted(colores):
        print(color)


def agregar_usuario():
    nombre = input("Ingresa el nombre del nuevo usuario: ")
    usuarios.append({'Nombre': nombre})
    print(f"Usuario {nombre} añadido exitosamente!")


def mostrar_usuarios():
    for usuario in sorted(usuarios, key=lambda x: x['Nombre']):
        print(usuario['Nombre'], usuario['Color'] if 'Color' in usuario else "Sin color")


def eliminar_usuario():
    while True:
        try:
            i = int(input("Ingresa el índice del usuario a eliminar: "))
            if i < 0 or i >= len(usuarios):
                print("Índice fuera de rango. Intenta de nuevo.")
                continue
            del usuarios[i]
            print("Usuario eliminado exitosamente!")
            break
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")


opcion = {
    '1': agregar_color,
    '2': agregar_usuario,
    '3': asignar_colores,
    '4': mostrar_colores,
    '5': mostrar_usuarios,
    '6': eliminar_usuario,
}

while True:
    print("\n1. Añadir color")
    print("2. Añadir usuario")
    print("3. Asignar colores")
    print("4. Mostrar colores")
    print("5. Mostrar usuarios")
    print("6. Eliminar usuario")
    print("7. Salir")
    seleccion = input("Selecciona una opción: ")
    if seleccion == '7':
        print("¡Adiós!")
        break
    elif seleccion in opcion:
        opcion[seleccion]()
    else:
        print("Opción inválida.")
