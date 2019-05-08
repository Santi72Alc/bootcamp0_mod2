"""
Función para sumar los 1ros (num) pasados por parámetros
"""

def sumaTodosNumeros ( num ):
	suma = 0
	for x in range(1, num+1):
		suma += x
	return suma

print(sumaTodosNumeros(20))

