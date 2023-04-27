num1,num2=100,50
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
op=int(input('¿que operacion?: ')) #op exporta funciones que son eficientes correspondientes a los operadores esenciales en python
match op: #match simplifica las operaciones donde se utiliza demasiado elif
    case 1: #case selecciona una entre un conjunto de expresiones que se van a evaluar y devuelve el valor de la expresion seleccionada
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)

# Se escoge una de las operaciones para obtener el resultado