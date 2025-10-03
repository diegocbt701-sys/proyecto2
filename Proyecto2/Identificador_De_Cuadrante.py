x = int(input("Ingrese la coordenada X: "))
y = int(input("Ingrese la coordenada Y: "))
if x == 0 or y == 0:
    print("Tenemos Un Problema, una De Las Coordenadas es 0.")
elif x == 0 and y == 0:
    print("Tenemos Un Problema, Ambas Coordenadas Son 0; El Punto Es El Origen.")
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante No. 1")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante No. 2")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante No. 3")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuadrante No. 4")
    