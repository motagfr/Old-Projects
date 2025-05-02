# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:23:22 2023

@author: M
"""
# type(round(7.89,1))
# x='Hello How are you?'
# x[1:4]

# i=0
# def IsCube():
#     a=int(input('Enter a number:'))

#     i=0
#     while i!=int(a/2):
#         i+=1
#         temp=i
#         if a%i==0 and a//i==i*i:
#             print('The number is a cube.',a,' is ',
#                   i,'raised to power 3.')
#             break
#         elif i==int(a/2):
#             print('The number is not a cube.')
#     return
# IsCube()
# print(i)
# print(temp)
# temp+=1
# print(temp)
# Q1
# def workshop_profit(n):
#     profit=n*(-6*2500+150000)-3000000
#     return profit
# #Q2
# is_profitable = workshop_profit(30) > 0
# is_profitable

# #Q3
# i=0
# while workshop_profit(i)<0:
#     i+=1
#     if workshop_profit(i)>0:
#         n_min = i
# n_min

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
z = []
# Method first
for a in x:
    y.append(a * 2)
print(y)

f"the vlues are {a}"

c = []
for b in x:
    c.append(hex(b**3))
print(c)

eval("12.03422") + 2

p = [a for a in x if a % 2 == 0]
dir(dict())

lis = [[1, 2], [3, 4], [5, 6]]
sum(sum(x) for x in lis)
