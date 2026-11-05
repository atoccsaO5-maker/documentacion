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
## Conociendo mas sobre funciones parametros y argumentos
sobre los parametros / argumentos nominales es ampliamente usado para distintaas configuraciones ya que se puede pasar solo loss argumentos que se usaran y dejar los parametros por defecto sino se van a modificar.
python
# tenenmos un programa que me permite acceder a internet que tiene parametros por defecto, sin embargo si se actualiza uno de los accesos se podran modificar o actualizar el valor.
##primer caso accesos por defecto 
def config(user="<usuario>",pass="<contraseña>",port="8080",bssid="wifi"):
    return"conectado a la red"
config()
## segundo caso 1 bssid cambio por el de "laboratorio"
def config(user="<usuario>",pass="<contraseña>",port="8080",bssid="wifi"):
    return"conectado a la red"
config(bssid="laboratorio1")
## reyner desea conectarse al wifi de ana luz, pregunta como se llama tu wifi y cual es su contraseña. respuesta el wifi es a56 y su contraseña es <contraseña>
def config(user="<usuario>",pass="<contraseña>",port="8080",bssid="wifi"):
    return"conectado a la red"
config(bssid="A56",pass="<contraseña>")

## conociendo *args y **kargs (empaquetado y desempaquetado de argumentos posicionales)
### desempaquetando argumentos posicionales
esta tecnica nos permite empaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar, imaginemos que nos piden una funcion para sumar n catidad de numeros la solucion seria empaquetar los argumentos y luego desenpaquetarlos para ello en la definicion de la funcion dentro de los parametros debemos usar el operador *`delante del nombre del parametro posicional esto hara que todos los argumentos se almacenen en una tupla()(lista[]`)esto nos permite recorrer dentro de sus elementos para poder desempaquetarlos y realizar las operaciones necesarias.
python
# deseamos crear una funcion que nos permita sumar n cantidad de numeros 
# es un numero variable puede ser 3,7,8 ........n
def suma(*args):
    #*args = (2,5,7,8,9)
    acumulado=0
    for i in args:
        acumulado += 1
    return acumulado
print(suma(2,5,7,8,9))

#### desempaquetando argumentos nominales

en este caso como en el anterior utilizaremos el operador *`la es el msimo sin embargo para desempaquetar argumentos nominales usaremos `**`delante del nombre del paramentro nominal diferencia del anterior esto se empaqueta en un diccionario ({clave:valor}`.
python

# debemos crear una funcion que me permita saber encontrar la persona con mayor calificacion.
def mejor_alumno(**kwargs):
    #**kwargs={'noemi':20,'eduardo':18,'david':19}
    nota_maxima=-1
    for alumno,nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno
    return mejor_alumno
mejor_alumno(noemi=20,eduardo=18,david=19)


## Funciones anonimas
las funciones anomnimas en python son llamados `lambda` , estas funciones tienen las siguientes proriedades.
1. se escribe en una unica sentencia `(linea)`.
2. no tiene nombre `(anonima)`.
3. su cuerpo conllva un `return` implicito.
4. pued recibir cualquier numero de parametros.

la estructura pera definir una funcion `lambda` es la siguiente:
1. escribir la palabra reservada `lambda`.
2. especificar la cantidad de parametros.
3.  luego indicar lo datos de retorno.
  
```python
lambda a,b: a+b
```
>[!TIP] puesto que esta funcion es anonima para ejecutar debemos almacenarla funcion en una variable.

```python
suma=lambda a,b : a+b
suma(3,6)
```

## Documentacion 
python nos permite documentar la funcion con el objtivo de explicar mjor determinadas zonas de nuestro codigo , para esto usamos una cadna de texto desúes de la definicon de una funcion,a esta cadena de texto s le conoc como `docstring` y esta delimitado por triples comillas `"""aqui el texto """`.

```python
def suma (a,b):
    """ 
    funcion para ralizar la suma d dos numeros
    """


## los docstring tambbien nos prmite explicar los parametros que recibe y los datos d salida.

def resta (a,b):
    """
    a=  un numero entero.
    b= un numreo entero.
    en ambos casos a,b no deb recibir valores menors 0.
    retornara un dato entero <int> positivo
    """
    return a-b

```

> [!WARNING] en el proceso de documentacion tener en cuenta de invluir a lo menos lo siguiente :
0. breve explicacion sobre la funcion.
1. especificacion de los siguiente parametros incluyendo  sus tipos.
2. rstriccions de la funcion.
3. el valor que retorna y sus caracteristicas.
