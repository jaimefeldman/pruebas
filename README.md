# Projecto pruebas en python

El proyecto prueba crea un paquete llamado `saludador` con le cuál se pretende crear un paquete de Python instalable en el sistema, que sea capaz de leer archivos que lleva en un subdirectorio llamado `resources/textos/archivo.txt` 

### Aspectos técnicos 

* dentro del proyecto debe existir un directorio con el nombre del paquete, en este caso `saludador`, dentro todos los subdirectorios del paquete como `launcher` `modulos` y `resources` cada directorio incluido saludador debe tener el archivo `__init__.py` para que Python lo considere un paquete válido y lo incluya en la compilación del paquete.

* se crea un archivo en la raíz del proyecto `pruebas` llamado `MANIFEST.in` el cual indica donde están los subdirectorios y archivos que deben ser copiados en el paquete.

Archivo MANIFEST.in:

```
recursive-include saludador/resources *
```

Luego es importante incluir en el archivo `setup.py`

`include_package_data=True,`

## Sistema de actualización
Intentando crear el sistema de actualización con github

## Instalación 

### Dentro del direcotrio del proyecto pruebas ejecutar:
```cmd
crea el paquete:
> python3 setup.py sdist

Instala el paquete en el sistema.
> pip install .
```

## Uso


## Contribuciones
Son bienvenidos las peticiones de pull, vea primero la lista de asuntos en discución de que le gutaría modificar.

## Liciencia
[MIT](https://opensource.org/licenses/mit-license.php)
