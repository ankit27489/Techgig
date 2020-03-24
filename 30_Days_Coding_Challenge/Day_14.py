# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:25:09 2020

@author: AnkitD
"""

'''
You need to input N words one on each line 
and output should be lexicographically sorted
i.e the words which comes as a output should be alphabetically sorted
'''
def main():

 n = int(input())
 word_list = []

 for i in range(n):
     word_list.append(input())

 word_list.sort()
 
 for word in word_list:
     if word_list[-1] == word:
         print(word, end="")
     else:
         print(word)

main()