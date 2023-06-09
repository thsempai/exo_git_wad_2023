from datetime import datetime
from functools import wraps

def print_return(function):
    @wraps(function)
    def wrapped_function(*args, **kwargs):
        result = function(*args, **kwargs)
        with open("log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} : {result}\n")

        return result

    return wrapped_function

@print_return
def cube(n):
    return n ** 3

if __name__ == "__main__":
    print(cube(5))        
    print(cube(20))        



