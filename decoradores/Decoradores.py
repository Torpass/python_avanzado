#ahora, un decorador es una funcion que recibe como parametro otra funcion, la modifica y retorna otra función
# diferente, aqui un ejemplo 

# Le pasamos como parametro una función
def decorador(func):
    def envoltura():
        print("Esto se añade a la funcion saludo")
        # ejecutamos la función 
        func()
    return envoltura

# funcion que actua cómo parámetro
def saludo():
    print("\nHola")


def run():
    # igual que un closure, "Saludo_" ahora va a actuar como una función independiente
    saludo_ = decorador(saludo)
    saludo_()
    saludo_()


if __name__ == "__main__":
    run()