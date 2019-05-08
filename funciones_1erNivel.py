def normal( x ) :
    return x

def cuandrado( x ):
    return x*x

def cubo( x ):
    return x*x*x

def sumaTodo( num, funcion ):
    suma = 0
    for x in range( num+1 ):
        suma += funcion( x )
        
    return suma


print( sumaTodo( 100, normal) )
print( sumaTodo(3, cubo) )