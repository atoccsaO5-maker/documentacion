# Ejercicio 1 para map()
# Recuerda: map() transforma todos los elementos de un iterable.
# Tienes una lista de números y quieres obtener una nueva lista con el cubo
# elevado a 3 de cada número.
numeros = [1, 2, 3, 4, 5]


def cubo(numero: int) -> int:
    return numero**3


cubos = list(map(cubo, numeros))
print("Cubos:", cubos)

# Ejercicio 2 para filter()
# Tienes una lista de temperaturas, algunas bajo cero, y quieres obtener una
# nueva lista con solo las temperaturas positivas.
temperaturas = [-5, 0, 10, 15, -3, 20]
positivas = list(filter(lambda temperatura: temperatura > 0, temperaturas))
print("Temperaturas positivas:", positivas)

# Ejercicio 3 combinado con map() y filter()
# Tienes una lista de números. Primero debes filtrar los números pares y luego
# usar map() para multiplicar por 10 los números pares.
numeros_combinados = [1, 2, 3, 4, 5, 6, 7, 8]
pares = filter(lambda numero: numero % 2 == 0, numeros_combinados)


def por_diez(numero: int) -> int:
    return numero * 10


pares_por_diez = list(map(por_diez, pares))
print("Pares por 10:", pares_por_diez)




