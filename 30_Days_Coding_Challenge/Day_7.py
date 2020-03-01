# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:36:01 2020

@author: AnkitD
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
# For this challenge, you are given a range and you need to find 
# how many prime numbers lying between the given range.
def main():

    a = int(input())
    b = int(input())

    flag = 0
    count = 0

    # Constraints
    if (a < 1 or a > 100000 or b < 1 or b > 100000):
        print("Invalid numbers")

    if (a < b):
        for i in range(a,b+1):
            flag = 0
            for divisor in range(2, int(i/2)):
                if (i/divisor == 0):
                    print("flag")
                    flag = 1
            if (flag == 0):
                print(i)
                count += 1
    print("Total Prime numbers are: ", count)

main()

