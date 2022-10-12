def run():
    a= input("Ingrese nombre: ")
    name = introducir_nombre(a)
    b = int(input("Cantidad de veces que se repite el nombre: "))
    print(name(b))

    c = int(input("dividendo: "))
    divison1 = dividendo(c)
    b = int(input("divisor: "))
    print(divison1(b))


def introducir_nombre(name: str):
    def multiplicador_nombre(int: int):
        assert type(name) == str, "Epa, pon un nombre"
        return name * int 
    return multiplicador_nombre


def dividendo(dividendo):
    def divisor(divisor):
        return dividendo / divisor
    return divisor

if __name__ == "__main__":
    run()