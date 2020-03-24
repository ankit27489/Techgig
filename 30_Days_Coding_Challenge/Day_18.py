# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:26:29 2020

@author: AnkitD
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

'''
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] 
such that sorting this subarray makes the whole array sorted.

13
1 2 4 7 10 11 7 12 3 7 16 18 19
'''

def main():

 start_index, end_index = 0, 0
 length = input() 

 l1 = input().split(" ")
 l2 = []
 for item in l1:
     l2.append(int(item))

 l1 = sorted(l2)

#  print("Unsorted List", l2)
#  print("Sorted List", l1)

 for i in range(len(l1)):
     if l1[i] != l2[i]:
         start_index = i
         break
 
 for i in range(len(l1)-1, -1, -1):
     if l1[i] != l2[i]:
         end_index = i
         break
#  print(start_index, end_index)   
 for i in range(start_index, end_index+1):
     if i == (end_index):
         print(l2[i], end="")
     else:
         print(l2[i], end=" ")

main()

