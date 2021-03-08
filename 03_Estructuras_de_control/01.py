#Ejercicio 1

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

if n1+n2>0:
    print("Suma positiva")
elif n1+n2<0:
    print("Suma negativa")
else:
    print("Suma es 0")
    
# Ejercicio 2

num = int(input("Número: "))        
if num%2==0:
    print("Número par")
else:
    print("Número impar")
    
# Ejercicio 3

mes = int(input("Mes: "))        
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print("31 días")
elif mes==4 or mes==6 or mes==9 or mes==11 :
    print("30 días")
elif mes==2:
    print("28 o 29 días")
else:
    print("Mes incorrecto")
    
# Ejercicio 4

user=input("Usuario: ")
passwd=input("Contraseña: ")        
if user=="yo" and passwd=="droga":
    print("Has entrado en el sistema")
else:
      print("pa fuera")
      
# Ejercicio 5

year = int(input("Año: "))        
if year%4==0 and year%100!=0 or year%400==0:
    print("Bisiesto")
else:
    print("No bisiesto")
    
# Ejercicio 6

lt = input("lt: ")        
if lt.isupper():
    print("Mayuscula")
else:
    print("No mayuscula")