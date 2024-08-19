
# Write a simple program that prints “Hello, World!”
# Create variables for your name, age, and a simple calculation (like adding two numbers).

# print('Hello, World')
name = 'Anjima'
age = 24

#adding two numbers
 
a = 10
b = 20
c = a + b
# print(c)


# Writing simple conditions (e.g., checking if a number is positive or negative)

def checkParity():
    number = int(input("Enter the number:"))
    if number == 0:
        print("Number is zero")
    elif number > 0:
        print("Number greater than zero")
    elif number < 0:
        print("Number is a negative number")

# checkParity()
# checkParity(-10)
# checkParity(22.22)
# checkParity(0)


#Basic string Operations
# Question: 
# Write a Python program that takes two strings as input from the user. 
# Concatenate them with a space in between and then print the length of the resulting string.
        
def stringOps():
    string1 = str(input("Enter first string"))
    string2 = str(input("Enter second string"))
    result = string1 + " " + string2
    print(len(result))

# stringOps()
    

# Question: Given the string "Python Programming", write a Python program to:
# Print the first character.
# Print the last character.
# Extract and print the substring "Programming" from the string using slicing.
    
def stringOperations(string):
    print(string[0])
    print(string[-1])
    print(string[6:])

# stringOperations("Python Programming")
    

# Question: Write a Python program that asks the user to input a string. Then:
# Convert the string to uppercase.
# Replace all occurrences of the letter 'a' with the letter 'o'.
# Print the final string.

def stringConversions(string):
    string1 = string.replace('a', 'o')
    new_string = string1.upper()
    print(new_string)

# stringConversions("rahnerya targeryan")
    

# Question: 
# Write a Python program that takes a sentence as input. 
# Split the sentence into words, then join them back into a single string with a hyphen - between each word. Print the resulting string.
    
def stringOperationstwo(sentance):
    new_sentance = sentance.split(" ")
    print(new_sentance)
    result = "-".join(new_sentance)
    print(result)

stringOperationstwo("My name is Alicent Hightower")


# Substring Check
# Question: Write a Python program that asks the user to input a sentence and a word. 
# Check if the word is present in the sentence and print an appropriate message.

def checkWord(sentance,word):
    print(word in sentance)

checkWord("Hanumankind is a mallu", "sharan")
checkWord("Fahim is a doctor", "doctor")









