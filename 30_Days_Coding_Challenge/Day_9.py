# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:39:32 2020

@author: AnkitD
"""

# Check if number is narcissit number

def main():

    n = input()
    power = len(n)
    total = 0
    
    n = int(n)
    x = n
    
    while(x>0):
        rem = x%10
        x = x/10
        
        total = total + (rem**power)
    
    if(n == total):
        print("True", end="")
    else:
        print("False", end="")

main()
