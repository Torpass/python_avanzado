from datetime import datetime
from typing import final

def run():
    cicle()


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_ =  final_time - initial_time 
        print(f"Pasaron {time_.total_seconds()} segundos")
    return wrapper




@execution_time
def cicle():
    for _ in range(1, 1000000000):
        pass    


if __name__ == "__main__":
    run()