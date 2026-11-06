## en la siguiente funcion deberan escribir la documentacion segun la convencion para el docstrings de funciones.

def multiplicar(*args)->list[int]:
    """
    Multiplica una cantidad variable de números enteros y devuelve una lista con los resultados.

    Args:
        *args (int): Una cantidad variable de números enteros a multiplicar.

    Returns:
        list[int]: Una lista que contiene los resultados de la multiplicación de los números proporcionados.
    
    Example:
        >>> multiplicar(1, 2, 3)
        [1, 2, 3]
        
        >>> multiplicar(4, 5)
        [20]
    """
    resultado: list[int] = []
    for i in args:
        resultado.append(i * 2)  # Ejemplo de operación de multiplicación
    return resultado

## funcion para hallar la potncia de un numero .
def potencia(n:int,p:int)->int:
    """
    Calcula la potencia de un número dado.

    Args:
        n (int): El número base.
        p (int): El exponente al que se elevará el número base.

    Returns:
        int: El resultado de elevar el número base a la potencia especificada.

    Example:
        >>> potencia(2, 3)
        8

        >>> potencia(5, 2)
        25
    """
    resultado :int=1
    for i in range(p):
        resultado *= n
    return resultado

