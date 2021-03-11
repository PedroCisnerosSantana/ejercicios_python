!#/usr/bin/python3
# Ejercicio 1

numero = int(input("Número: "))
cont = 1
while (cont<=10):
	print ("%d * %d = %d" % (cont, numero, cont * numero))
	cont += 1
 
# Ejercicio 2

num = int(input("Número: "))
fact=1
for i in range(2,num+1):
	fact*=i
print("El resultado es %d" % fact)

# Ejercicio 3

secret = 5
num = int(input("Número: "))
while num!=secret:
    if num>secret:
        print("menos")
    else:
        print("mas")
    num=int(input("Número: "))
print ("Has acertado")

# Ejercicio 4

for num in range(1,6):
    	for cont in range(1,11):
		print ("%2d * %d = %2d" % (cont, num, cont * num))
	print()
 
# Ejercicio 5

num = int(input("Número: "))
primo = True
for cont in range(2,num):
    if num%cont==0:
        primo=False
        break
if primo:
    print("primo")
else:
    print("No primo")