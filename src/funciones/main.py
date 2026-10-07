# Crear un programa que me permita mostrar un mensaje personalizado.
# Crear una función similar a la función print de Python que reciba un mensaje
# y lo muestre en pantalla.

"""Función que muestra mensajes personalizados en pantalla."""


def mostrar_mensaje(mensaje: str) -> None:
    """Muestra un mensaje personalizado."""
    print(mensaje)


def main() -> None:
    """Ejecuta una ejemplo de la función personalizada."""
    mostrar_mensaje("¡Hola! Este es mi mensaje personalizado.")


if __name__ == "__main__":
    main()


