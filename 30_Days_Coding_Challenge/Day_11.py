# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:47:08 2020

@author: AnkitD
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
'''
For this challenge, you need to take a string as an input from the stdin, 
count the number of uppercase and lowercase letters 
and print them to the stdout.
'''
def main():

 stmt = input()
 up,lo = 0, 0
 
 for a in stmt:
     if a.isalpha():
         if a.isupper():
             up = up+1
         elif a.islower():
             lo = lo+1
         
 print(up)
 print(lo, end="")

main()


