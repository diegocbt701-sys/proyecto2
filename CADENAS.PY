#TEXTO_VARIADO= "PALABRAS ALEATORIAS +-EDKKM+633. #5+++6"
#PRINT=(type(TEXTO_VARIADO))

#podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
#print("""funcionamiento de \
 #     programa:(opciones)
  #      -1 para acceder a opciones
   #        -2 para salir
    #   """)
#-----------------------------------------------------------
#subscripting e indexado
# texto = 'pyton'
# print(texto[0])
# print(texto(5))
# print(texto(-1))
# print(texto(-6))

# print(texto{6}) #errror, no podemos acceder a una posicion que no existe
# print(texto(-7)) #error, no podemos acceder a una posicion que no existe

# letra= texto[0]
# print(letra)

# #text[2]='T' #error, las cadenas son inmutables

# letra = 'T'
# print(letra)

# texto_compuesto= letra + texto[1] #concatenacion
# print(texto_compuesto)
#-----------------------------------------------------------

#slicing o substringing
#texto = 'Python'
# print(texto[0:3]) #impresion de los caracteres desde la posicion 0 hasta la 3 (sin incluir la 3) osea pyt
# print(texto[0:-3]) #impresion de los caracteres desde la posicion 0 hasta la -3 (sin incluir la -3) osea pyt otra vez
# print(texto[0:-2]) #impresion de los caracteres desde la posicion 0 hasta la -2 (sin incluir la -2) osea Pyth
# print(texto[2:]) #impresion de los caracteres desde la posicion 2 hasta el final osea thon
# print(texto[:3]) #impresion de los caracteres desde el inicio hasta la posicion 3 (sin incluir la 3) osea pyt

# print(texto[-3::-1]) #impresion de los caracteres desde la posicion -3 hasta el inicio (sin incluir la -3) osea htyP

#print(texto[::-1]) #impresion de los caracteres desde el final hasta el inicio (sin incluir el final) osea nohtyP
#print(texto[2::50]) #impresion de los caracteres desde la posicion 2 hasta el final (sin incluir el final) con un salto de 50 osea thon
#print(texto[2::2])
#-----------------------------------------------------------
#cadenas y formatos 

texto = 'Hola Mundo! BuenasTardes'
# print(texto.lower()) #sirve para imprimir todo en minusculas
# print(texto.upper()) #sirve para imprimir todo en mayusculas
# print(texto.capitalize()) #sirve para imprimir la primera letra en mayuscula y el resto en minusculas
# print(texto.title()) #sirve para imprimir la primera letra de cada palabra en mayus
# print(texto.swapcase()) #sirve para intercambiar mayusculas por minusculas y viceversa
# texto = texto.upper()
# print(texto)

print('{} + {} + ={}'.format(2,3,2+3)) #forma antigua de formatear cadenas
print('{} + {} + = {}'.format('hola', 'mundo', 'hola mundo')) #forma antigua de formatear cadenas
print('{:.3f}+{:.4f}={}'.format(2,3,2+3)) #sirve para limitar el numero de decimales
print('{1} +{0} ={2}'.format(2 , 3, 2+3)) #sirve para cambiar el orden de los argumentos
print('{1} + {0} = {2}'.format('hola', 'mundo', 'Hola Mundo')) #sirve para cambiar el orden de los argumentos
print('{:d} = {:b} = {:o} = {:x}'.format(15,15,15,15)) #sirve para convertir un numero decimal a binario, octal y hexadecimal
