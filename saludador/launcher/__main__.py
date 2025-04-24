import sys 
import saludador.launcher as main_module
import saludador.modulos.examples as examples
import saludador.modulos.files as files
import saludador.modulos.math  as calc
import saludador.modulos.updater as updater

from termcolor import colored

def main(args=None):
    print("[", colored("Inicio de la app de pruebas", "green"), "], version:", main_module.__version__)

    # Creando objeto saluador.
    saludo_obj = examples.Saludador()

    # Probando los modulos.
    print("sumando 234 + 345 = ", calc.suma(234, 345))	

    if args is None:
        args = sys.argv[1:]
    
    # Si existen argumentos, haga algo...
    if len(args) > 0:
        pass	

    # Intenando leer el archivo de resources/archivos/archivo.txt
    files.read_file('textos/archivo.txt')    

    # Intentando actualizar la aplicación.
    updater.update()

if __name__ == "__main__":
    exit(main())

