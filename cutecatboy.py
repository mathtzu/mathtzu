import sys
import math

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