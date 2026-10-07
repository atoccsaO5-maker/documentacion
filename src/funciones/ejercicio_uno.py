# crear un programa que me permita desarrollar las 4 operaciones básicas de una calculadora.
def suma(a: float, b: float) -> float:
    return a + b

def resta(a: float, b: float) -> float:
    return a - b

def multiplicacion(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b



# en una sola operacion las 4 operaciones basicas de una calculadora que funcione.
def operaciones(n:list,o:str):
    if o == "+":
        return suma(n)
    print(operaciones([4,5,20,40],"+"))  