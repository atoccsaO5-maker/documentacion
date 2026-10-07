# Funciones python

las funcions nos permiten ordenar mejor el codigo y reutilizar cunado sea necesario.
```python
# ejemplos . deseamos crear un programa qu nos permita sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=50
numero_cuatro:int=30
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)

```
como hacemos reutilizable el ejercicio anterio con funciones.
la caracteristica de una funcion en python  es la siguiente :
1. debe comenzar con la palabra reservada `def`.
2. debe de tener un  nombre que de a enterder que realizara la funcion.
3. debera tener parametros estos estaran enserrados en parentecis`()` . 
4. no todas las funciones recibiran parametros aun asi debra los parentecis `()`.
5. las funciones deberan retornar datos a travez de la palabra reservada `return` .
   
```python
# crea un programa que me érmita sumar dos numeros.

def sumar(a,b):
    return a+b

print(sumar(78+70))
print(sumar(30+45))
```
## Ejecución

```bash
python src/funciones/main.py
```

## Enfoque

- Funciones pequeñas y bien definidas.
- Entradas y salidas claramente documentadas.
- Reutilización desde otros módulos.
