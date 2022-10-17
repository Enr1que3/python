'''En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.'''

from functools import reduce

numerosImpares=[1,2,3,4,5,6,7,8,9]

def sumaImpares(suma):
    if suma % 2 !=0:
        return True

resultado=filter(sumaImpares,numerosImpares)

print(list(resultado))
