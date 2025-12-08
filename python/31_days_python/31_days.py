#DAY 1
# Given an array, we have to find the largest element in the array.
# Examples
# Example 1:  
# Input: arr[] = {2, 5, 1, 3, 0}  
# Output: 5  
# Explanation:  
# 5 is the largest element in the array.

# Example 2:  
# Input: arr[] = {8, 10, 5, 7, 9}  
# Output: 10  
# Explanation:  
# 10 is the largest element in the array.


def findLNo(a):
    a.sort()
    return a[-1]

# print(findLNo([33, 62, 10, 34]))

#optimal solution

def fnlNo(a):
    max_num = a[0]
    for i in range(1, len(a)):
        if a[i] > max_num:
            max_num =a[i]
    return max_num

# print(fnlNo([56, 62, 10, 34]))

#qn 2
# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.
# Examples
# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: True.
# Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

# Example 2:
# Input: N = 5, array[] = {5,4,6,7,8}
# Output: False.
# Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.
# Here element 5 is not smaller than or equal to its future elements.
            
def checkSorted(a):
    c = a[:]
    print(c)
    a.sort()
    b = a
    print(b)
    if c == a:
        return True
    else :
        return False

# print(checkSorted([10, 2, 0, 3 ]))


#optimal solution
def ifSorted(a):
    if len(a) == 0 or len(a) == 1:
        return True
    else:
        for i in range(0, len(a)):
            if a[0] > a[i+1]:
                return False
            else:
                return True
# print(ifSorted([10, 2, 0, 3 ]))

############################## DAY 2 ############################
# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
# Examples
# Example 1:  
# Input: [1, 2, 4, 7, 7, 5]  
# Output:  
# Second Smallest : 2  
# Second Largest : 5  
# Explanation:  The elements are sorted as 1, 2, 4, 5, 7, 7.  
# Hence, the second smallest element is 2, and the second largest element is 5.

# Example 2:  
# Input: [1]  
# Output:  
# Second Smallest : -1  
# Second Largest : -1  
# Explanation:  Since there is only one element in the array, it is both the largest and smallest element.  
# Therefore, there is no second smallest or second largest element present.


def secondSM(a):
    b = sorted(set(a))
    return b[1] , b[-2]
        

# print(secondSM([1, 2, 4, 7, 7, 5]))


#qn2
# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
# Examples
# Example 1:  
# Input: arr[] = 1 2 3 4 5, num = 3  
# Output: 2  `
# Explanation: 3 is present at the 2nd index of the array.

# Example 2:  
# Input: arr[] = 5 4 3 2 1, num = 5  
# Output: 0  
# Explanation: 5 is present at the 0th index of the array.

def findNum(a, num):
    for i in range(0, len(a)):
        if a[i] == num:
            return i
    else:
        return -1
    

print(findNum(a = [1,2,3,4,5], num = 10))

            


