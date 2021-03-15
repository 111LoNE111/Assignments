#1.Write a program which will find all such numbers which are divisible by 7 but are not a
#   multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
#   in a comma-separated sequence on a single line.
i=2000
while i>=2000 and i<=3200:
    if i%5 !=0 and i%7==0:
        print(i, end=',')
    i+=1




#2.Write a Python program to accept the user's first and last name and then getting them
#  printed in the the reverse order with a space between first name and last name.
Name=input()

class Order_reversal:
    def __init__(self,Name):
        self.name=Name
    def reverse(self):
        new_name=self.name[::-1]
        return new_name


print(Order_reversal(Name).reverse())


#3. Write a Python program to find the volume of a sphere with diameter 12 cm.
diameter=12
from math import *
class Sphere:
    def __init__(self,diameter):
        self.diameter=diameter
    def volume(self):
        radius=((self.diameter)/2)
        volume=(4/3)*pi*(radius**3)
        return volume
print(Sphere(diameter).volume(),'cm^3')