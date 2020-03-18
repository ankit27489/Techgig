# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:07:06 2020

@author: AnkitD
"""


'''
take a matrix as an input from the stdin , 
transpose it and print the resultant matrix to the stdout.

'''

def main():

 size = input().split(" ")
 size = [int(item) for item in size]

 mat = []

 for row in range(size[0]):
     mat.append(input().split(" "))


 T_mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

 for item in T_mat:
     if T_mat[size[1]-1] == item:
         item = " ".join(item)
         print(item.rstrip(), end="")
     else:
         print(" ".join(item))
     

main()

