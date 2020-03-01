# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:20:09 2020

@author: AnkitD
"""

# For this challenge, you will take an integer input from stdin, 
# store it in a variable and  calculate the number of digits in the number 
# using division operator.
def main():

 n = int(input())
 x = n

 digit = 0

 while(x>0):
     x = int(x/10)
     digit += 1
 print(digit, end="")

main()