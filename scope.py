# Los socpes como tal son el alcance que tiene una variables, ya sea a nivel local o a nivel global 

y = 5 

def run():
    print(y)
    suma_y()

def suma_y():
    y =  6
    print(y)
 

if __name__ == "__main__":
    run()