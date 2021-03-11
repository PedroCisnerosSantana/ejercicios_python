!#/usr/bin/python3
def guardar_agenda(l_agenda,**kwargs):
    	l_agenda.append(kwargs)
	return l_agenda	

def main():
	agenda=[]
	cantidad = int(input("Cuanta gente vas a meter?: "))
	for i in range(cantidad):
		contacto={}
		contacto["nombre"]=input("Dime el nombre: ")
		contacto["telefono"]=input("Dime el teléfono: ")
		campo=input("Dime otro campo: ")
		while campo!="*":
			contacto[campo]=input("Dime un valor: ")
			campo=input("Dime un campo:")
		agenda=guardar_agenda(agenda,**contacto)
	print(agenda)	

if __name__ == '__main__':
	 main()