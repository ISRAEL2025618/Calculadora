"""
(1) suma
(2) resta
(3) multiplicacion
(4) division
"""
def calculadora(num1, num2, op):
    print('bienvenido a la calculadora de python')
    if op == 1:
        print(f'El resultado de la suma de {num1} y {num2}: {num1 + num2}')
    elif op == 2:
        print(f'El resultado de la resta de {num1} y {num2}: {num1 - num2}')
    elif op == 3:
        print(f'El resultado de la multiplicacion de {num1} y {num2}: {num1 * num2}')
    elif op == 4:
        print(f'El resultado de la division de {num1} y {num2}: {num1 / num2}')
    else:
        print('te equivocaste de opcion')

    calculadora(50,50,1)
    calculadora(50,50,2)
    calculadora(50,50,3)
    calculadora(50,50,4)













    

