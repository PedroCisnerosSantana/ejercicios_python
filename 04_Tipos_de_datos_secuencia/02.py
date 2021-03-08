!#/usr/bin/python3
def ejercicio1():
    cadena = input("Cadena: ")
    caracter = input("Carácter: ")
    print(caracter.join(cadena))
    
def ejercicio2():
    cadena = input("Cadena: ")
    caracter = input("Carácter: ")
    for i in range(10):
        cadena = cadena.replace(str(i),caracter)
    print(cadena)
    
def ejercicio3():
    cad=input("Cadena:")				

    lista=cad.split(" ")
    for palabra in lista:
        print (palabra[0],end="")
    print()

    for palabra in lista:
        print (palabra.capitalize(),end=" ")
    print()			

    for palabra in lista:
        if palabra.startswith("a") or palabra.startswith("A"):
            print (palabra,end=",")
    print()
    
def ejercicio4():
    cad1=input("Cadena 1:")
    cad2=input("Cadena 2:")	
    if cad1.find(cad2)>-1:
        print ("cad2 es subcadena de cad1")
    else:
        print ("cad2 no es subcadena de cad1")			

    print(cad1 if cad1<cad2 else cad2)
    
def ejercicio5():
    cad1=input("Cadena:")	
    if cad1.lower()==cad1[::-1].lower():
        print("palindromo")
    else:
        print("no palindromo")