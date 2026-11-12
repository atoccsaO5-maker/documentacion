## crear una funcion cuyos parametros sean un entero , una listas de entros y flotantes y la funcion retornara una lista de enteros o flootante
def my_function(n: int, lst: list[int | float]) -> list[int | float]:
    return [item * n for item in lst]