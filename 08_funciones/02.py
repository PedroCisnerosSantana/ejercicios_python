!#/usr/bin/python3

def calcular_segundos(horas,minutos,segundos):
    return horas*3600+minutos*60+segundos	

def calcular_horas(segundos):
	horas = segundos // 3600
	segundos-=horas*3600
	minutos = segundos // 60
	segundos-=minutos*60
	return horas,minutos,segundos

def calcular(*args):
	if len(args)==1:
    	return calcular_horas(args[0])
	elif len(args)==3:
		return calcular_segundos(*args)
	else:
		raise TypeError("Se espera 1 o 3 parámetros")

def buscar(l_agenda,**kwargs):
    	lista_aciertos=[]
	for contacto in l_agenda:
		aciertos=0
		for campo,valor in kwargs.items():
			if campo in contacto and contacto[campo]==valor:
				aciertos+=1
		if aciertos==len(kwargs):
			lista_aciertos.append(contacto)
	return lista_aciertos	

def main():
	...
	
	## Búsqueda
	filtro={}
	campo=input("Introuzca un campo para buscar:")
	while campo!="*":
		filtro[campo]=input("Introuzca valor a buscar:")
		campo=input("Introuzca otro campo a buscar:")
	print(buscar(agenda,**filtro))