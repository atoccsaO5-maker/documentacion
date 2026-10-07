"""Ejemplo básico de programación orientada a objetos."""


class Persona:
    """Representa una persona."""

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def presentar(self) -> str:
        """Devuelve una presentación de la persona."""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


def main() -> None:
    """Crea y muestra una instancia de Persona."""
    persona = Persona("Ana", 25)
    print(persona.presentar())


if __name__ == "__main__":
    main()
