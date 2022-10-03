f=open('./ejercicio1.txt','w')
lista=[
    'texto ',
    'de ',
    'practica con ',
    'python\n'
]
f.writelines(lista)
f.close()