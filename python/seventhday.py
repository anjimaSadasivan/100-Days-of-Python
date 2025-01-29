#recursion with simple programs

#factorial of a number

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(3))

#fibonacci series

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 5
fib_num = [fibonacci(i) for i in range(0,n)]
# print(fib_num)




# Accept a string input and print its reverse.
def reverseString(sentance: str):
    return sentance[::-1]

print(reverseString("hello kuttu"))



# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def addOne(digits: list):
    result = int("".join(map(str, digits)))
    res = result + 1
    digits = [int(x) for x in str(res)]
    return digits