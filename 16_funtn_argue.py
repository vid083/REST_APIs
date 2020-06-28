def add(x, y):
    result = x + y
    print(result)


add(2, 3)  



def say_hello():
    print("Hello!")


say_hello("Bob")  



def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Bob")
say_hello()  

# -- Keyword arguments --


def say_hello(name):
    print(f"Hello, {name}!")


say_hello(name="Bob")  

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=3)
divide(15, 0)
divide(15, divisor=0)