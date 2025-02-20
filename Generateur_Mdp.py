# Created by DragonNoir_off
# link to GitHub profile : https://github.com/DragonNoir-off
# Last edit -> 20/02/2025
# version [ 1 ]

from time import *
from math import *
from random import *

import os

Symbol_Table = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+','[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?']
Character_Table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Generate_PassWord(Character_total, Table):
    PassWord = ""
    
    for i in range(Character_total):
        PassWord = PassWord + str(Table[randint(0, len(Table)-1)])
        
    print("\n")
    print("Password :")
    print(PassWord)
        
def Setup_Table(Character_total,Character_bool,Maj_bool,Number_bool,Symbol_bool):
    Table = []
    if Character_bool == True:
        for i in Character_Table:
            Table.append(i)
    if Maj_bool == True:
        for i in Character_Table:
            Table.append(i.upper())
    if Number_bool == True:
        for i in range(10):
            Table.append(i)
    if Symbol_bool == True:
        for i in Symbol_Table:
            Table.append(i)
    
    Generate_PassWord(Character_total, Table) # generate the pass word with the specific table than contain every character possibility depend on the parameter selected

def Check_Valid_input(_input, _type):
    if _type == 1:
        if _input == "yes" or _input == "no":
            return True
        else:
            return False
    
    if _type == 2:
        try:
            _input = int(_input)
            if int(_input) < 0: return False
            return True
        except:
            return False

def Display_Choice(Character_total,Character_bool,Maj_bool,Number_bool,Symbol_bool):
    print("Total Character the Password contain : ",Character_total,"\n")
    print("Parameter : ")
    if Character_bool == True: print("✅ Alphabet Character")
    else: print("❌ Alphabet Character")
    if Maj_bool == True: print("✅ Capital Alphabet Character")
    else: print("❌ Capital Alphabet Character")
    if Number_bool == True: print("✅ Number")
    else: print("❌ Number")
    if Symbol_bool == True: print("✅ Symbol")
    else: print("❌ Symbol")

def Check_input(_input, _type):
    if _type == 1:
        if _input == "yes": return True
        else: return False

def Setup():
    
    os.system('cls' if os.name == 'nt' else 'clear') # clear le terminal
    
    Character_total = 0
    Maj_bool = False
    Number_bool = False
    Symbol_bool = False
    Character_bool = False
    
    __input = "" # define
    
    print("[[-- Input the parameter of the password --]]\n")
    
    __input = input("Number of character than contain the password : ")
    while not Check_Valid_input(__input, 2):
        print("invalid input, please input a valid answer -> (number) \n")
        __input = input("Number of character than contain the password : ")
    Character_total = floor(int(__input))
    
    __input = input("is the password contain Alphabet Character ? (yes/no) -> ")
    while not Check_Valid_input(__input, 1):
        print("invalid input, please input a valid answer -> (yes/no) \n")
        __input = input("is the password contain Alphabet Character ? (yes/no) -> ")
    Character_bool = Check_input(__input, 1)
    
    __input = input("is the password contain Alphabet Capital Letter ? (yes/no) -> ")
    while not Check_Valid_input(__input, 1):
        print("invalid input, please input a valid answer -> (yes/no) \n")
        __input = input("is the password contain Alphabet Capital Letter ? (yes/no) -> ")
    Maj_bool = Check_input(__input, 1)
    
    __input = input("is the password contain Symbole ? (yes/no) -> ")
    while not Check_Valid_input(__input, 1):
        print("invalid input, please input a valid answer -> (yes/no) \n")
        __input = input("is the password contain Symbole ? (yes/no) -> ")
    Symbol_bool = Check_input(__input, 1)
    
    __input = input("is the password contain Number ? (yes/no) -> ")
    while not Check_Valid_input(__input, 1):
        print("invalid input, please input a valid answer -> (yes/no) \n")
        __input = input("is the password contain Number ? (yes/no) -> ")
    Number_bool = Check_input(__input, 1)
    
    print(">---------------------------------------------------------------------<") # separator ( just esthetical )
    
    Display_Choice(Character_total,Character_bool,Maj_bool,Number_bool,Symbol_bool) # display parameter of the pass word
    
    Setup_Table(Character_total,Character_bool,Maj_bool,Number_bool,Symbol_bool) # insert every possibility of character than can be use in the pass word into a table
    
Setup()
