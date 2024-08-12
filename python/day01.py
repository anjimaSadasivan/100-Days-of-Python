# sum of 2 nos
a = int(input("first number"))
b = int(input("second number"))

def sumofNos(a,b):
    sum = a+b
    print(sum)
    return sum

sumofNos(a,b)

# sum of n numbers
# find the sum of first 25 integers


n = int(input("Enter number"))
print(n)
def sumof(n):
    sum = n*(n+1)/2
    print(sum)
    return sum

sumof(n)


# sum of nos between A and B
a = int(input("Enter first number"))
b = int(input("Enter second number"))

def sumBetweenNos(a,b):
    sum = ((b-a+1)*(a+b))/2
    print(sum)
    return sum

sumBetweenNos(a,b)




# factorial of a number:


def factorial(n):
    if n>=1:
        fact = 1
        for i in range(1, n+1):
            fact *= i 
    else:
        print("Fact dont exist")
    print(fact)    
    return fact

factorial(5)



# odd number or even number-Find Parity of number

def parityofNumber(n):
    if n % 2 == 0:
        print("Numer is even")
    else:
        print("Number is odd")
    
    return 0

parityofNumber(129)

    

#prime number or not

def is_prime(n):
   if n<= 1:
      print("Not a Prime")
      return False
   else:
      for i in range(2, int(n ** 0.5) + 1):
         if n % i == 0:
            print("It is no a prime number")
            return False
      print("Its a prime number")
      return True
        
is_prime(2)
is_prime(7)
is_prime(5)
is_prime(4)
is_prime(129)





   



   
         
   
      