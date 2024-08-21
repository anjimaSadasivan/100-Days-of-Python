# Reverse a String
# Question: Write a Python program to reverse a given string using a for loop.

# prepend method
def reverseString(string):
    rev_string = ""
    for i in string:
        rev_string = i + rev_string
    print(rev_string)

# reverseString("ammu")

#alternmate method-USING RANGE IN FOR LOOP

def reverseStringtwo(string):
    rev_string = ""
    for i in range(len(string)-1, -1, -1):
        rev_string = rev_string + string[i]
    print(rev_string)
# reverseStringtwo("NOGORD")
    

#USING WHILE LOOP
    
def reverseStringwithwhile(string):
    rev_string = ""
    n = len(string)
    i = 0
    while i <= n-1:
        rev_string =  string[i] + rev_string
        i +=1
    print(rev_string)
# reverseStringwithwhile("ammu")


# Count Digits in a Number
# Question: Write a Python program that counts the number of digits in an integer using a while loop.

def countDigits(n):
    if isinstance(n, int):
        i = 0
        n1 = str(n)
        noofdigits = 0
        while i <= len(n1)-1:
            noofdigits = 1 + noofdigits
            i +=1
        print(noofdigits)
    else:
        print("Not an integer")
# countDigits(80782523289446759232)
        
# Question: Write a Python program to generate the Fibonacci series up to n terms using a for loop.
        
def fibonnaci(n):
    n1 = 0
    n2 = 1
    series = []
    series.append(n1)
    series.append(n2)
    for i in range(0, n-1):
        next_terms = series[i] + series[i+1]
        series.append(next_terms)
    print(series)
# fibonnaci(4)

# Question: Write a Python program to print all prime numbers between 1 and 100 using nested for loops.

# def printPrimeNumbers():











    



        


