#Question
# Write a program that takes two numbers as input, performs arithmetic operations, and displays the results.

def calculator(num1,num2):
    addition = num1 + num2
    subs = num1 - num2
    multiply = num1*num2
    divide = num1/num2
    modulo = num1 % num2
    print(addition,subs,multiply,divide,modulo)

# calculator(10,5)


# Write a Python program to:
# Take your name and age as input and print a greeting message.
def greeting(name):
    yourname = name
    print("Wishes {}".format(yourname))
# greeting("Daemon")



# Calculate the area of a rectangle (length × width).

def area(length, breadth):
    area = 2*(length + breadth)
    print(area)
# area(2,3)

# Check if a number is even or odd.

def checkParity(number):
    if not isinstance(number,int):
        print("Niether even nor odd")
    elif number % 2 == 0:
        print("even number")
    elif number % 2 != 0:
        print("odd number")
    
# checkParity(4)
# checkParity(-3)
# checkParity(0)
# checkParity(3.5)


# Question: Write a Python program to print all even numbers between 1 and 50 using a for loop.

def printEvennosbw(n1,n2):
    for i in range(n1, n2+1):
        if i % 2 == 0:
            print(i)

# printEvennosbw(1,50)


# Sum of Natural Numbers
# Question: Write a Python program that calculates the sum of all natural numbers up to a given number n. Use a while loop.
            
def sumofnumberswithwhile(n):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i +=1 
    print(sum)
# sumofnumberswithwhile(5)

#Alternate method

def sumofnos(n):
    sum = n*(n+1)/2
    print(sum)

# sumofnos(5)
    
# Sum of even nos using while loop
    
def sumofevennos(n):
    sum = 0
    i = 2
    while i <= n:
        if i % 2 == 0:
            sum = sum + i
        i +=1
    print(sum)
            

# sumofevennos(5)
    
# Question: 
# Write a Python program to display the multiplication table of a given number using a for loop.
    
def multiplicationtable(n):
    for i in range(1, 11):
        table = n * i
        print(table)

# Question:
# Write a Python program to calculate the factorial of a given number using a while loop.
        
def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact = fact * i
        i +=1
    print(fact)  

factorial(5)




