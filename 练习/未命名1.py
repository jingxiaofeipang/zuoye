# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:07:29 2024

@author: 25051
"""

def getfrequency(s):
    '''接收一个字符串，返回一个3个整数的元组，分别代表数字，大小写字母和其他符号出现的次数
    '''
    digits,alphabets,others = 0,0,0
    for i in s:
        if i >= '0' and i <='9':
            digits += 1
        
        elif i >= 'a'and i<='z' or i >= 'A' and i<='Z':
            alphabets += 1
            
        else:
            others += 1
            
    return (digits,alphabets,others)

print(getfrequency('jing123...'))
            



def isplindrome(text):
    if len(text)<=1:
        return True
    if text[0] != text[-1]:
        return False

    else:
        return isplindrome(text[1:-1])
    
sentences = ('deed','dad','need','rotor','civic','eye','redivider','noon','his','difference','a')

for sentence in sentences:
    print(sentence,end='')
    
    if isplindrome(sentence):
        print("是回文数")
        
    else:
        print("不是回文数")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    