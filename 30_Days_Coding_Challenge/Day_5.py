# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:11:13 2020

@author: AnkitD
"""

# For this challenge, you need to take an integer value as input from stdin, 
# calculate its factorial and print the result to the stdout. 1

def main():

 fact = 1
 n = int(input())
 for i in range(1,n+1):
     fact = fact*i
 print(fact,end="")

main()