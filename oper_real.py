# Curso: Introducción a la programación.
# Lenguaje: Python. Por: Mauricio Maca Chagüendo
# Temas: Entrada y salida de datos.
#        input, int, float, bool


def main():
    print('Entrada y salida de datos\n')
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    c = a + b
    print(f'Suma:\n{a} + {b} = {c}')             # Suma usando una variable auxiliar
    print(f'{a:10.3f} + {b:10.3f} = {c:10.3f}')  # Modificación del formato de salida
    print(f'Diferencia:\n{a} - {b} = {a - b}')   # De forma directa
    print('\nFin del programa.')


if __name__ == '__main__':
    main()


# Ejercicio: Modifique el programa para que realice otras operaciones aritméticas.
#            ¿Para que sirve la secuencia "/n" al imprimir una cadena?
# Recuerde que la función input permite leer solo cadenas desde el teclado, se deben
# usar las funciones float, int, bool para realizar la respectiva conversión de tipos.


# Revisar https://docs.python.org/3/tutorial/inputoutput.html