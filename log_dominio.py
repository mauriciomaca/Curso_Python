# Curso: Introducción a la programación.
# Lenguaje: Python. Por: Mauricio Maca Chagüendo
# Temas: Condicionales.
#        Evaluar el logaritmo en base 10 en su dominio.
#        f-string, imprimir resultado con 5 decimales.

from math import log10


def main():
    print('Calculo del logaritmo en base 10.')
    x = float(input('Ingrese un número real positivo: '))
    if x > 0:
        y = log10(x)
        print(f'Log10({x}) = {y:.5f}')
    else:
        print(f'El número {x} no está en el dominio de Log10.')
    print('Fin del programa.')


if __name__ == '__main__':
    main()

