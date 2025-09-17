"""
This program explain about
python version, basic printing statement and
comment lines
"""
import sys
print(sys.version)

print("Hi, welcome to python playwright")

print("My name is: Rakshitha")

#variables
x=6
x="Python"
print(x) #Here value of x will be python bcs it has been replaced

"""
Casting is used to specify the data type of variable
"""
x=str(3)
print(x)

y=int(3)
print(y)

z=float(3)
print(z)
print(z+ y)
print(z- y)
print(z*y)

# type() is used to get the type of a variable
a=5
b="hi"
print(type(a))
print(type(b))

#assigning multiple var in single line
x,y,z=10,20,30
print(x,y,z)

x=y=z=3
print(x,y,z)

#list
places = ["mysore","banglore","chickmanglore"]
print(places)
print(type(places))
print(places[2])

#concatenate
x="My "
y="name "
z=" is rakshitha"
print(x,y,z)
print(x + y + z)

#concatenation should be done for same data types
"""
x=(1)
y="python"
print(x+y)
 we will get error here bcs of different data type, to overcome that x=str(1)
"""
print(10>100)
