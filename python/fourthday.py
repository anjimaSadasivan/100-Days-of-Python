# Question: Write a Python program to print all prime numbers between 1 and 100 using nested for loops.
import math
def primeNumbers(n):
    list_of_prime = []
    for i in range(2, n+1):
        is_prime = True
        for num in range(2, int(math.sqrt(i)+1)):
            if i % num == 0:
                is_prime = False
                break
        if is_prime == True:
            list_of_prime.append(i)
    print(list_of_prime)

# primeNumbers(10)
            


# Question: 
# Write a Python program to find the sum of the digits of a given number using a while loop.

def sumofDigits(n):
    new_num = str(n).replace(".","")
    length = len(new_num)
    sum = 0
    i = 0
    while i < length:
         sum +=  int(new_num[i]) 
         i +=1
    print(sum)
        



# sumofDigits(124.34)
    


# Question: Write a Python program to print the following pattern using nested for loops:

# *
# * *
# * * *
# * * * *
# * * * * *
    

#method-1
def printPattern(n):
    for i in range(1, n+1):
        print("*" * i)

#method-2
        
def printPatterntwo(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()
        


# printPatterntwo(5)
        

#Check if a string has all unique characters
        
def checkifStringhasUnique(string):
    new_list = list(string)
    n = len(new_list)
    new_list.sort()
    for i in range(0, n-1):
        is_uni = True
        if new_list[i] == new_list[i+1]:
            is_uni = False
            print("Not unique chara")
            break
    if is_uni == True:
            print("All chara is unique")

# checkifStringhasUnique("raquelr")


#Given two strings, check if one is the permuatation of other

def checkPermuatation(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("p")
    else:
        print("not p")
    

# checkPermuatation("abc","abc")
# checkPermuatation("listen","silent")
# checkPermuatation("abcd","abc")
# checkPermuatation("hello","world")
# checkPermuatation("aabbcc","abcabc")


#Write a method to replace all spaces in a string with "%20"
#ex "Mr John Smith", 13 Input
# "Mr%20John%20Smith"
        

def replaceChara(string, length):
    new_string = string.replace(" ", "%20")
    print(new_string)
    

replaceChara("Mr John Smith",13)

