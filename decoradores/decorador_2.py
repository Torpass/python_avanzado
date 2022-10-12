# Acá lo que hago es usar un concepto algo importante que es el "azucar sintactico", hace que nuestro código sea mucho más estético y de facíl compresión, por ejemplo con el "@" lo que indicamos es que la funcion que vamos a crear debajo, ya va a estar decorada y podemos invocarla de una vez. 

def run():
    saludo()


def decorador(func):
    def envoltura():
        print("Esto se añade a la funcion saludo")
        func()
    return envoltura


@decorador
def saludo():
    print("Hola mundo")


if __name__ == "__main__":
    run()