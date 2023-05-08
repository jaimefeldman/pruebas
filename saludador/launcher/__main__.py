import sys, saludador.modulos
from termcolor import colored

def main(args=None):
    print("[", colored("Inicio de la app de pruebas", "green"), "]")
    print("* probando la organización de paquetes en python.")	

    # Creando objeto saluador.
    saludo_obj = saludador.modulos.Saludador()

    # Probando los modulos.
    print("sumando 234 + 345 = ", saludador.modulos.suma(234, 345))	

    if args is None:
        args = sys.argv[1:]
    
    # si existen argumentos, haga algo...
    if len(args) > 0:
        pass	

    # intenando leer el archivo de resources/archivos/archivo.txt
    saludador.modulos.read_file('textos/archivo.txt')    

if __name__ == "__main__":
    exit(main())

