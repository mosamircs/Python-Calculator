# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:13:51 2018

@author: {MoSamirCS}
"""
def calculator(x,y,op):
    if op=='+':
        z=x+y
        int(z)
        print("the result of sum operation is ") 
        print(z)
    elif op=='-':
        z=x-y
        int(z)
        print("the result of sub operation is ") 
        print(z)
    elif op=='*':
        z=x*y
        int(z)
        print("the result of mul operation is ")
        print(z)
    elif op=='/':
        z=x/y
        int(z)
        print("the result of div operation is ")
        print(z) 
    else:
        print("Not Supported operation yet")
print("This Calcuator can Add,Sub,Mul,Div 2 Numbers!!!")
first=int(input("Enter The first value: "))
second=int(input("Enter the second value: "))
operation=input("Enter the operation: ")
calculator(first,second,operation)