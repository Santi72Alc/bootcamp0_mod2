
def max( *l ):
    """
    Devuelve el máximo de los valores pasador a la función por parámetro
    Si no se pasan valores devuele None
    """
    if len( l ) == 0:   # NO se han pasado valores
        return None
    m = l[0]
    for i in l[1:]:   # desde el 2do componente hasta el final
        if i > m:
            m = i
    return m


def min( *l ):
    """
    Devuelve el mínimo de los valores pasador a la función por parámetro
    Si no se pasan valores devuele None
    """
    if len( l ) == 0:   # NO se han pasado valores
        return None
    m = l[0]
    for i in l[1:]:   # desde el 2do componente hasta el final
        if i < m:
            m = i
    return m


def media( *l ):
    """
    Devuelve media aritméyica de todos los valores pasador a la función por parámetro
    Si no se pasan valores devuele None
    """
    if len( l ) == 0:   # NO se han pasado valores
        return None
    suma = 0
    for i in l:   # desde el 2do componente hasta el final
            suma += i
    return suma/len(


print( max ( 1, 6, 7, 2) )
print( min( 4,3,7,23,1,5) )
print( media( 5,7,6,8 ) )
