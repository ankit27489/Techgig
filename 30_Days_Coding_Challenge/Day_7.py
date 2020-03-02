# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:32:28 2020

@author: AnkitD
"""

# For this challenge, you are given a range and you need to find 
# how many prime numbers lying between the given range.
def main():

    a = int(input())
    b = int(input())

    count = 0

    for num in range(a,b+1):
        if num > 1:
            for divisor in range(2, num):
                if(num%divisor == 0):
                    break
            else:
                count += 1

    print(count,end="")              

main()