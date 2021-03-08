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
    lista=['Di', 'buen', 'dia', 'a', 'papa']
    print(lista[::-1])
    
def ejercicio3():
    lista=['Di', 'buen', 'dia', 'a', 'papa',"hola","papa","buen","dia"]	
    cadena = input("Cadena: ")
    if cadena in lista:
        print("La cadena está en la lista")
    else:
        print("La cadena no está en la lista")	

    print(lista.count(cadena))	

    cadena2 = input("Cadena a reemplazar: ")
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