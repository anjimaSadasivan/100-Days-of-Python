#generate fibonacci sequence

#using loop which is more efficient and understandable and easy tro debug

def fibonacci(n):
    fibo_list = [0,1]
    for i in range(2, n+1):
        next_numbers = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(next_numbers)
        
    print("Fibonacci Sequenece", fibo_list)
    
fibonacci(4)

#using recursion-
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = [fibonacci_recursive(i) for i in range(n)]
print("Fibonacci sequence:", fib_numbers)



#permutation


def permuatation(string):
    new_string = string.lower()
    new_list = list(new_string)
    n = len(new_list)
    for i in range(0, n//2):
        if new_list[i] != new_list[n-i-1]:
            print("Not a Permutation")
            return False
        else:
            print("permutation")
            return True
        
permuatation("ammu")
permuatation("Malayalam")


#Implement an algorithm to find if the string has all unique characters

Illustration-1

def checkforUnique(string):
    new_string = string.lower()
    new_list = list(new_string)
    new_list.sort()
    n = len(new_list)
    print(new_list)
    for i in range(0, n-1):
        if new_list[i] == new_list[i+1]:
            print("String is not unique")
            return False
    print("String is unique")
    return True

checkforUnique("hello")



# reverse a string

def reverse(string):
    array = list(string)
    array.reverse()
    rev_str = ''.join(array)
    print(rev_str)
    
reverse("chuttu")







#leap year or not

def leapYear(n):
    if n%4 == 0:
        # print(n%4)
        print("Year is leap")
    else:
        print("Year is not leap")
leapYear(2024)
leapYear(2022)



#check if string is an anagram


#Illustration-1
def anagramCheck(string_one, string_two):
    string_one_small = string_one.lower()
    string_two_small = string_two.lower()
    array_one = list(string_one_small)
    array_two = list( string_two_small)
    array_one.sort()
    array_two.sort()
    n = len(string_one_small)
    m = len(string_two_small)
    if n != m:
        print("Not an anagram")
        return False
    else:
        if array_one == array_two:
            print("Its an anagram")
            return True
        else:
            print("Not an anagram")
            return False
        

        
#Illustration-2
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)




        
 


    



        









