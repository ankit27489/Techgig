# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 00:07:25 2020

@author: AnkitD
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

# you need to take an integer input and store it in a variable of your choice and checks whether this number is an Armstrong number or not. 
# If yes print 'True' else print 'False'.


def main():

    a = int(input())
    n = a
    new_num = 0

    while (n>0):
        digit = n%10
        new_num = (digit**3) + new_num
        n = int(n/10)

    if (a == int(new_num)):
        print("True", end="")
    else:
        print("False")

main()