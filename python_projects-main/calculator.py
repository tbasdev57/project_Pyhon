print("Simple calculator app")

def add(x,y):
    '''returns the addition of two numbers'''
    return x + y
def diff(x,y):
    '''returns the difference of two numbers'''
    return x - y
def prod(x,y):
    '''returns the product of two numbers'''
    return x * y
def div(x,y):
    '''returns the quotient of two numbers'''
    return x / y

finished = False

while not finished:
    result = 0
    array = [None, None, None]
    array[0] = int(input('Introduce el primer número '))
    array[1] = input('Qué operación deseas efectuar? (+, -, *, / )')
    array[2] = int(input('Introduce el segundo número '))

    if array[1] == '+':
        result = array[0] + array[2]

    elif array[1] == '-':
        result = array[0] - array[2]

    elif array[1] == '*':
        result = array[0] * array[2]

    elif array[1] == '/':
        result = array[0] / float(array[2])

    else: print(array[1] + ' no es un comando valido.')

    print('El resutlado es ' + str(result))

    again = ''
    valid_input = False
    while not valid_input:
        again = input('Deseas hacer otra operación? ')

        if again == 'y':
            valid_input = True
        elif again == 'n':
            valid_input = True
            finished = True
        else:
            print('La respuesta debe ser "y" o "n"')