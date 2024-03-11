def ingresar_datos():
    while True:
        print('Ingrese una evaluación del 1 al 5:')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Ingrese un comentario:')
                comment = input()
                post = f'Puntuación: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Ingrese una puntuación del 1 al 5.')
        else:
            print('Ingrese la puntuación como un número.')

def visualizar_resultados():
    print('Resultados hasta el momento:')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

while True:
    print('Seleccione la operación que desea realizar:')
    print('1: Ingresar puntuación y comentario')
    print('2: Ver resultados hasta el momento')
    print('3: Salir')
    num = input()

    if num.isdecimal():
        num = int(num)
        if num == 1:
            ingresar_datos()
        elif num == 2:
            visualizar_resultados()
        elif num == 3:
            print('Saliendo del programa.')
            break
        else:
            print('Ingrese un número del 1 al 3.')
    else:
        print('Ingrese un número del 1 al 3.')
