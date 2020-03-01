# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:04:15 2020

@author: AnkitD
"""

def main():
    age = int(input())
    if (age < 10):
        print('I am happy as having no responsibilities.',end="")
    elif (age >= 10 and age < 18):
        print('I am still happy but starts feeling pressure of life.',end="")
    else:
        print('I am very much happy as i handled the pressure very well.',end="")
main()

