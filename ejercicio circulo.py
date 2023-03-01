from math import pi
radio=float(input('Ingrese el radio del círculo en cm: '))
area=round(pi*radio**2,3)
perimetro=round(2*pi*radio,3)
print('El área del círculo es de',area,'centímetros cuadrados')
print('El perímetro del círculo es de',perimetro,'centímetros')
