#Escribe una funcion que pueda decir si un año es bisiesto(numero entero) o no

def bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print('Año es bisiesto')
            else:
                print("Año no bisiesto")
        else:
            print("Año bisiesto")
    else:
        print("Año no bisiesto")

year =int(input("ingrese el año"))
bisiesto(year)