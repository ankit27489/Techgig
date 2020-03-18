# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:49:45 2020

@author: AnkitD
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
'''
This program takes two integers from user ( base number and a exponent) 
and calculates the power. Instead of using loops to calculate power, 
this program uses recursion to calculate the power of a number.
'''

def calc_power(n, p, val=1):
    if(p == 0):
        print(val, end="")
    else:
        val = val*n
        p = p-1
        calc_power(n, p, val)
        

def main():
 inp = input().split(" ")
 n = int(inp[0])
 p = int(inp[1])

 calc_power(n, p)
main()


