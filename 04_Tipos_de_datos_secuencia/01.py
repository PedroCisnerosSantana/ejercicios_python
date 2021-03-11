!#/usr/bin/python3
def ejercicio1():
    num = int(input("Número: "))
    lista = []
    while num>0:
        lista.append(num)
        num = int(input("Número: "))		
    print("Máximo: %d" % max(lista))
    for n in [x for x in lista if x % 2 == 0]:
        print(n)
        
def ejercicio2():
    lista=['Di', 'queda', 'alcohol', 'en', 'casa']
    print(lista[::-1])
    
def ejercicio3():
    lista=['Di', 'queda', 'alcohol', 'en', 'casa',"queda","alcohol","en","casa"]	
    cadena = input("Dime una palabrita: ")
    if cadena in lista:
        print("La palabra está en la lista")
    else:
        print("La palabra no está en la lista")	

    print(lista.count(cadena))	

    cadena2 = input("Palabra a reemplazar: ")
    apariciones=lista.count(cadena)
    pos=0
    for i in range(0,apariciones):
        pos=lista.index(cadena,pos)
        lista[pos]=cadena2
    print(lista)
    
def ejercicio4():
    lista = [2,3,4,1]
    lista2 = lista[:]
    lista.sort()
    if lista==lista2:
        print("Lista ordenada")
    else:
        print("Lista no ordenada")