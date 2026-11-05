# haciendo un usao de lambda crear una funciones que me muestre un mensaje personalizado
mensaje = lambda nombre: f"Hola, {nombre}!"
print(mensaje("Alice"))

## crear una funcion para calcular el area de un rectangulo siendo la formula area = base * altura

area_rectangulo = lambda base, altura: base * altura
print(area_rectangulo(5, 10))

# crear una funcion que verifique si un numro es par o impar
es_par = lambda numero: "Par" if numero % 2 == 0 else "Impar"
print(es_par(13))
print(es_par(24))