import random
import math
#MonteCarloPi

puntos_en_el_cuadrado = int(input("Cuantos puntos quieres en el cuadrado? : "))
puntos_dentro_del_circulo = 0

for _ in range (0, puntos_en_el_cuadrado):
    puntoX = random.uniform(-1, 1)
    puntoY = random.uniform(-1, 1)
    if (puntoX**2 + puntoY**2) <= 1:
        puntos_dentro_del_circulo += 1
        
pi = 4 * (puntos_dentro_del_circulo/puntos_en_el_cuadrado)    
print("pi es igual a {0}".format(pi))
pi_nuevo = 4 *(math.pi/4)
#print(pi_nuevo)


