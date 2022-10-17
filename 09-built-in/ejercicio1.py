'''Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.'''
listaPais=[]
unicoPais=[]

for i in range(3):
    listaPais.append(str(input("Escribe el pais: ")))
    print("Tus paises son: \n",str(listaPais))

   
    
