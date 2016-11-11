#!/bin/python
import sys

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

  
'''
1 <= a < s < t < b <= 100000

s - a = distance from the house to the apple tree
b - t = distance from the house to the orange tree

if  s <= (a + s) <= t:
    apple
elif s <= (b + d) <= t:
    orange
'''

apple_count = 0
orange_count = 0
for d in apple:
    if (s <= (a+d)) and ((a+d) <= t):
        apple_count += 1
for d in orange:
    if (s <= (b+d)) and ((b+d) <= t):
        orange_count += 1

print(apple_count)
print(orange_count)