# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:19:37 2020

@author: AnkitD
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
'''
For this challenge, you need to take array and an integer as an input, 
check for pair in array with sum as that of an integer and 
if you find those two numbers in the array return true else return false.
'''

def check_val():
 size = int(input())
 l1 = []

 items = input().split(" ")
 
 for item in items:
     l1.append(int(item))

 value = int(input())
 print("value is: ", value)

 l1.sort()

 for i in range(len(l1)):
     first = l1[i]
     i = i+1
     print("index is: ", i)
     while (i < len(l1)):
         total = first + l1[i]
         print("Total is: ", total)
         if(total == value):
#             print("True")
             return "True"
         i += 1
 return "False"

def main():
    
    result = check_val()
    print(result, end="")

main()

