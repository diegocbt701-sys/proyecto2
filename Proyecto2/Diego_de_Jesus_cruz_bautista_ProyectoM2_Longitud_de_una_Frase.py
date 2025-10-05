palabra = input("Ingresa Una Palabra Por Favor: ") #esta linea solicita al usuario que ingrese una palabra, input la almacenara el valor ingresado en la variable palabra
x = len(palabra) #len cuenta la cantidad de caracteres en la variable palabra y lo almacena en la variable x
if x >= 4 and x <= 8: print(f"¡Palabra correcta! La longitud está entre 4 y 8 letras, tiene {x} letras.") #esta linea se encarga de analizar la variable x si la longitud de la palabra es entre 4 y 8 letras, imprime un mensaje de confirmación y la cantidad de caracteres escritos
elif x < 4: print(f"Hacen falta letras. Solo tiene {x} letras.") #si la longitud de la palabra es menor de 4 letras, imprime un mensaje indicando que faltan letras
else: print(f"Sobran letras. Tiene {x} letras.") #si la longitud de la palabra es mayor de 8 letras, imprime un mensaje indicando que sobran letras
