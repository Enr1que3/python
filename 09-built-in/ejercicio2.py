'''En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.'''

from functools import reduce
numeros =[1,3,5,7,9,11,13]

def impares(x):
    impar=filter(numeros)

res=impares(numeros)

print(res)

    
        
