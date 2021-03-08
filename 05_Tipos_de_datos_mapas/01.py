!#/usr/bin/python3
codigo = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
    }	

def ejercicio1():
    dict = {}
    frase = input("Frase:")
    lista_palabras=frase.split(" ")
    for palabra in lista_palabras:
        if palabra in dict:
            dict[palabra]+=1
        else:
            dict[palabra]=1	

    for campo,valor in dict.items():
        print (campo,"->",valor)

def ejercicio2():
    palabra = input("Palabra:")
    lista_codigos = []
    for caracter in palabra:
        if caracter.islower():
            caracter=caracter.upper()
        lista_codigos.append(codigo[caracter])	
    print(" ".join(lista_codigos))

def ejercicio3():
    morse=input("Morse:")
    lista_morse=morse.split(" ")
    palabra = ""
    for cod in lista_morse:
        letra=[key for key,valor in codigo.items() if valor==cod][0]
        palabra=palabra+letra
    print(palabra)

def ejercicio4():
    gustos={}
    nombre = input("Nombre:")
    while nombre!="*":
        gusto=input("Gusto:")
        lista_gustos=gustos.setdefault(nombre,[gusto])
        if lista_gustos!=[gusto]:
            gustos[nombre].append(gusto)
        nombre = input("Nombre:")
    print(gustos)