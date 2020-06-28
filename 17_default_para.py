def add(x, y=3):
    print(x + y)


add(5)  # 8
add(5, 8)  
add(y=3)  


default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  

default_y = 4
print(default_y)  

add(2) 