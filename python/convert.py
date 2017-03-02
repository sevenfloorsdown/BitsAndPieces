#!/usr/bin/python
from string import ascii_uppercase

#convert base 36 number to decimal

BASE = 36

def buildcodex():
    codex = []
    for i in range(0, BASE):
        if i < 10:
            codex.append(str(i));
        else:
            codex.append(ascii_uppercase[i-10]);
    return codex;
               
def convert(s):
    codex = buildcodex()  
    y = s[::-1]
    a = 0
    for i in range(0, len(y)):
        a += codex.index(y[i]) * BASE**i
    return a
        
print convert('1BP49B')
#print convert('123456')




    



