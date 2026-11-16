# 1. Funciones basicas
def calcular_area_rectangulo(base, altura):
	area = base * altura
	return area


print(calcular_area_rectangulo(5, 3))
print(calcular_area_rectangulo(4.5, 2))


# 2. Parametros nominales y por defecto
def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
	precio_con_descuento = precio * (1 - descuento)
	precio_final = precio_con_descuento * (1 + impuesto)
	return precio_final


print(calcular_precio_final(100, descuento=0.05))


# 3. Type-hints
def obtener_promedio(numeros: list[int]) -> float:
	total = 0
	for numero in numeros:
		total = total + numero
	promedio = total / len(numeros)
	return promedio


print(obtener_promedio([10, 20, 30]))


# 4. Empaquetado posicional (*args)
def unir_frases(*args):
	frase = ""
	for palabra in args:
		frase += palabra + " "
	return frase.strip()


print(unir_frases("Aprender", "Python", "es", "util"))


# 5. Empaquetado nominal (**kwargs)
def generar_perfil_usuario(**kwargs):
	perfil = ""
	for clave, valor in kwargs.items():
		perfil += f"{clave}: {valor}\n"
	return perfil.strip()


print(generar_perfil_usuario(nombre="Ana", edad=25, pais="Peru"))


# 6. Funciones anonimas (lambda)
es_par = lambda numero: numero % 2 == 0
print(es_par(8))
print(es_par(7))


# 7. Documentacion (docstring)
def calcular_potencia(base: float, exponente: float) -> float:
	"""Calcula una potencia.

	Args:
		base (float): Numero que se eleva.
		exponente (float): Potencia no negativa.
	Raises:
		ValueError: Si el exponente es negativo.
	Returns:
		float: Resultado de elevar la base al exponente.
	"""
	if exponente < 0:
		raise ValueError("El exponente no debe ser negativo.")
	return base**exponente


print(calcular_potencia(2.0, 3.0))


# 8. Closure (clausura)
def crear_validador_limite(limite_maximo: int):
	def validar(numero):
		return numero <= limite_maximo

	return validar


validador = crear_validador_limite(100)
print(validador(80))
print(validador(120))


# 9. Programacion funcional (map)
precios: list[float] = [10.5, 20.0, 50.0, 5.99]
precios_con_aumento = list(map(lambda precio: precio * 1.10, precios))  # noqa: C417
print(precios_con_aumento)


# 10. Programacion funcional (filter)
palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"]
palabras_largas = list(filter(lambda palabra: len(palabra) > 4, palabras))
print(palabras_largas)
