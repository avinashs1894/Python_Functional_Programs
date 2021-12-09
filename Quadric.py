'''
Created on 05-Dec-2021

@author: DELL
'''
from math import sqrt



a= int(input("enter the value of A:"))
b= int(input("enter the value of B:"))
c= int(input("enter the value of C:"))

delta=(b*b)-(4*a*c)

root1 = (-b+sqrt(delta))/2*a
root2 = (-b-sqrt(delta))/2*a

print("Value of delta is:",delta)
print("Value of Root1 is:", root1)
print("Value of Root2 is:", root2)