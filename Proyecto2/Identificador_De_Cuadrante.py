x = float(input("Ingrese la coordenada X: "))
y = float(input("Ingrese la coordenada Y: "))
#en las primeras dos lineas se solicita al usuario que ingrese las coordenadas x y y, y se convierten a flotantes con float()
#para identificar en que cuadrante se encuentra el punto (x,y) utilizaremos las condicionales if, elif y else
if x == 0 or y == 0: #if comenzara la estructura condicional, verificando si alguna de las coordenadas es 0
    print("Tenemos Un Problema, una De Las Coordenadas es 0.") #en el caso de que alguna de las coordenadas ingresadas sea 0, se imprime un mensaje indicando que hay un problema
elif x == 0 and y == 0: #elif continuara la estructura condicional, verificando si ambas coordenadas son 0
    print("Tenemos Un Problema, Ambas Coordenadas Son 0; El Punto Es El Origen.") #en el caso de que ambas coordenadas sean 0, se imprime un mensaje indicando que el punto es el origen
elif x > 0 and y > 0: #elif continuara la estructura condicional, verificando si ambas coordenadas son positivas
    print("El punto se encuentra en el cuadrante No. 1") #en el caso de que ambas coordenadas sean positivas, se imprime un mensaje indicando que el punto se encuentra en el cuadrante No. 1
elif x < 0 and y > 0: #elif continuara la estructura condicional, verificando si x es negativo y y es positivo
    print("El punto se encuentra en el cuadrante No. 2") #en el caso de que x sea negativo y y sea positivo, se imprime un mensaje indicando que el punto se encuentra en el cuadrante No. 2
elif x < 0 and y < 0: #elif continuara la estructura condicional, verificando si ambas coordenadas son negativas
    print("El punto se encuentra en el cuadrante No. 3") #en el caso de que ambas coordenadas sean negativas, se imprime un mensaje indicando que el punto se encuentra en el cuadrante No. 3
elif x > 0 and y < 0: #elif continuara la estructura condicional, verificando si x es positivo y y es negativo
    print("El punto se encuentra en el cuadrante No. 4") #en el caso de que x sea positivo y y sea negativo, se imprime un mensaje indicando que el punto se encuentra en el cuadrante No. 4

