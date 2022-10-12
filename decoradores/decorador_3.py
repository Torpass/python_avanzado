def run():
    print(mensaje('Pastor'))


def mayus(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@mayus
def mensaje(nombre):
    return f"Hey {nombre}, te ha llegado un mensaje"


if __name__ == "__main__":
    run()