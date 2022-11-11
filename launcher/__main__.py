import sys, modulos
from termcolor import colored

def main(args=None):
    print("[ Inicio de la app de pruebas ]")
    print("* probando la organización de paquetes en python.")	

    # Creando objeto saluador.
    saludo_obj = modulos.Saludador()

    # Probando los modulos.
    print("sumando 234 + 345 = ", modulos.suma(234, 345))	

    if args is None:
        args = sys.argv[1:]
    
    # si existen argumentos, haga algo...
    if len(args) > 0:
        pass	


if __name__ == "__main__":
    exit(main())

