# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:34:19 2020

@author: AnkitD
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
'''
For this challenge, you need to take input of two numbers , 
calculate their greatest common divisor (GCD) and print it to the stdout.
'''

import math

def main():
    no = input().split(" ")
    n1 = int(no[0])
    n2 = int(no[1])

    print(math.gcd(n1, n2), end="")
main()


