# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:40:10 2020

@author: AnkitD
"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

'''
you need to take 2 matrices as an input from the stdin , 
add them and print the resultant matrix to the stdout.
'''
def main():

 mat_1, mat_2, sum_mat, sum_row = [], [], [], []
 n = input().split(" ")
 # m = input()
 
 for i in range(int(n[0])):
     mat_1.append(input().split(" "))

 p = input().split(" ")

 for i in range(int(p[0])):
     mat_2.append(input().split(" "))

 if (n == p):
    #  print("Equivalent matrices")
    for row in range(int(n[0])):
        for i in range(int(n[0])):
            sum_row.append(int(mat_1[row][i]) + int(mat_2[row][i]))
        sum_mat.append(sum_row)
        sum_row = []


 for i in range(3):
     row = " ".join([str(elem) for elem in sum_mat[i]])
     if (i == 2):
         print(row, end="")
     else:
         print(row)

main()

