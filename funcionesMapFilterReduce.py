from functools import reduce

lista = [ 1, 3, -1, 15, 9 ]

# Función map permite ejecutar una función para cada uno de los componentes de la lista
# devolviendo la nueva lista
listaDobles = map(lambda x : x*2, lista)

# función filter devuelve SÓLO los elementos de la lista que coinciden con la condición
# indicada en lambda
listaPares = filter(lambda x : x % 2 == 0, lista)

listaMultiplosDeTres = filter( lambda x : x % 3 == 0, lista)


# Función reduce (x, y) aplica a cada par de elementos hasta reducir a un sólo valor
listaSumaDobles = reduce(lambda x, y : x*2 + y*2, lista)


print("Lista original : {}".format(lista))

print("Dobles - map : {}".format( list( listaDobles ) ) )

print("Pares - filter : {}".format( list( listaPares ) ) )
print("Mult. de 3 - filter : {}".format( list( listaMultiplosDeTres ) ) )

print("Suma Dobles - reduce : {}".format( listaSumaDobles ) )