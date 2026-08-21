import sys
import math
import random

print(sys.version)
print("ill meow for krisiya")
#meowww >.<


if 273 > 1:
    print("the number is greater")


print("are you"); print("no i wasnt")

# end= "" is used to make the next print statement in the same line
print("if life is a movie", end= "")
print(" then youre the best part ")

print(4*2)

# double asterisk for exponents
a = 5.3
b = 3
print( a * b ** b )

#outputting multiple variables
topics = ["calc2", "diffeq", "statics"]
x, y, z = topics
print( x, y ,end = " " )
print( z, y )

#global variables (pede doble "x" variable na gamitin pero ung isa inside sa variable lang naggamit ung laman ng x)
def myfunc():  
    x = "transform"
    print("to become the best version of urself you must " + x)

myfunc()

print("The first obstacle is", x)

# global variable is iniiba ung value ng variable lahatan kahit nasa loob ng function
def myfunc2():
    global z
    z = "lowkey"
myfunc2()

print(z)
# instead na staitcs lumabas naging lowkey

#try factorial
K = math.factorial(7)
print(type(K))

print(x == "transform")
# inunahan ko na HAHAHAHA
print(type(a * b ** b ))

print(type(1j))

# Create variables data types toh
x = 5
y = 3.14
z = "Hello"

# Print the data type of each variable
print(type(x))
print(type(y))
print(type(z))

def myfunc3():
    global x
x = 10
myfunc3()

# changes the int to float kahit whole number na hehe
print(x)
J = complex(x)

print(J)
print(type(J))

print(random.randrange(1, 100))

def meowtzu():
    global y
y = 3.5415

meowtzu()

a = int(y)
print(a, end= " ")
print(type(a))
# the number always rounds towards zero, postive numbers get smaller, while negative actually get bigger (closer to zero) when rounded down.

def solely():
    global x
    global y
    global z
    x = 5
    y = 3.14
    z = 2+3j

solely()
print(type(x), type(y), type(z))
# isa isa dapat naka "type" para ma print lahat ng data types, bawal ung type(x, y, z) lang kasi eerrr

