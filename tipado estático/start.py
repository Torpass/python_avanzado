from cgi import print_arguments
import string


def run():

    Usuario: string = "Pastor"
    Contraseña1: int = 12
    Contraseña2: string = "123"
    print(basic_suma(Contraseña1, Contraseña2))
    print(Usuario, Contraseña1, Contraseña2)
    print(f"Contrseña int : {type(Contraseña1)}")
    print(f"Contrseña str : {type(Contraseña2)}")
 
 
def basic_suma(a: int, b: str) -> string: 
    suma = a+b
    return suma


if __name__ =="__main__":
    run()