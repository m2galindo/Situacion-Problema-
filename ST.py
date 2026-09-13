"""
ST 
Equipo  
Marco Alejandro Galindo de la Cruz A00845553
Daniela Lozano 
Julio 
"""
import numpy as np

np.set_printoptions(suppress=True)

#  Datos 
x = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])            # cemento 
z = np.array([10, 10, 10, 10, 10, 15, 15, 15, 15, 15])  # agua 
y = np.array([12, 22, 32, 42, 52, 10, 18, 28, 35, 45])  # resistencia 

# Construir la matriz A (columna de unos , cemento , agua)
n = len(y)
unos = np.ones(n)
A = np.column_stack([unos, x, z])

print("Matriz A =")
print(A)

# Vector b 
b = y
print("\nVector b =")
print(b)

# Transpuesta de A
At = A.T
print("\nA^T (A transpuesta) =")
print(At)

# Construir A^T A multiplicando A^T por A
AtA = At @ A
print("\nA^T A =")
print(AtA)

# Construir A^T b multiplicando A^T por b
Atb = At @ b
print("\nA^T b =")
print(Atb)

#Resolver el sistema de ecuaciones 
xcoef= np.linalg.solve(AtA, Atb)
print("\nCoeficientes (beta0, beta1, beta2):")
print(xcoef)
