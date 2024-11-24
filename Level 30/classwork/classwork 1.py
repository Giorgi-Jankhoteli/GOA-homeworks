# function
# def - define - განსაზღვრა / შექმნა
# ----------------------------------
from turtle import*

def square():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    exitonclick()

square()    
square()    
square()    
square()    
# ------------------------------------
def mult():
    return 5 + 5

print(mult())
# -------------------------------------
# პარამეტრი
# არგუმენტი

def plus(a, b):
    return a + b

print(plus(5, 7))
print(plus(1, 2))
print(plus(10, 12))

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(5))
# -------------------------------------