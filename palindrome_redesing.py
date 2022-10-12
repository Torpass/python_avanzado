#rediseñando el programa palindromo hecho anteriormente, pero ahora con tipado estático de python 

def run():
    palabra = recibir_palabra()
    print(palindrome(palabra))
    

def palindrome(string: str) -> bool:
    return string==string[::-1]
     

def recibir_palabra():
    palabra = input("Ingrese la palabra a comprobar: ")
    palabra = palabra.replace(' ', '').lower()
    return palabra

if __name__ == "__main__":
    run()