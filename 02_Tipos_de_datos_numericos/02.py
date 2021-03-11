!#/usr/bin/python3

from math import pi

# Ejercicio 1

name = input("Como tu te llama mamabicho: ")
print("Yo soy %s mamawebo"%name)

# Ejercicio 2

base = float(input("Cual es la base shulo: "))
altura = float(input("Y la altura: "))
pe = 2*base + 2*altura
ra = base * altura
print("Resultado: Perimetro=%.2f Area=%.2f" % (pe,ra))

base = float(input("Dime la base: "))
la = float(input("Dime un lao: "))
lb = float(input("Ahora el otro: "))
altura = float(input("Y la altura: "))
pe = base + la + lb
ra = base * altura / 2
print("Resultado: Perimetro=%.2f Area=%.2f" % (pe,ra))

# Ejercicio 3

radio = float(input("Radio del circulo: "))
print("Resultado: Area=%.2f Perimetro=%.2f" % (pi*radio**2,2*pi*radio))

# Ejercicio 4

n1 = float(input("Primer numerito: "))
n2 = float(input("Segundo numerito: "))
print("Suma:%d\nresta:%d\nmultiplicacion:%d\ndivision:%.2f"%(n1+n2,n1-n2,n1*n2,n1/n2))

# Ejercicio 5

word = input("Introduce la palabra magica: ")
print((word+" ")*1000)

# Ejercicio 6

minutos = int(input("Introduce los minutos: "))
print("Horas:%d - Minutos:%d" % (minutos/60,minutos%60))