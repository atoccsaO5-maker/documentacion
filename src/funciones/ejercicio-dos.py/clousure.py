## crear una funcion que me permita ingresar nombre , apellido y me retorne un mensaje con ambos datos
def creador(nombre: str):
    def apellido(apellido: str) -> str:
        return f"Hola {nombre} {apellido}, bienvenido!"
    return apellido

alumno = creador("Juan")
mensaje = alumno("Pérez")
print(mensaje)



## usando closure para crear una funcion multiplicador que revisa por paramtro el factor que devuelva una funcion que me permita multiplicar cualquir numero por ese factor
def multiplicador(factor: int):
    def multiplicar(numero: int) -> int:
        return numero * factor
    return multiplicar