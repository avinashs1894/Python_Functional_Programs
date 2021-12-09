'''
Created on 06-Dec-2021

@author: DELL
'''

import math

v=int(input("Input wind speed in Km:"))
t=int(input("Input temperature of wind:"))

w=35.74+0.6215*t+(0.4275*t+35.74)*(math.pow(v,0.16))

print("Wind chill condition is:", int(round(w)))