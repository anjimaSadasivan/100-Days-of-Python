#questions from striver sheet
def findValue(n:int, exp:list):
    for i in exp:
        x = 0
        if "++" in i:
            x += 1
        elif "--" in i:
            x -= 1
    return x
        
n = 1
exp = ["++x"]

# print(findValue(n,exp))

#A. Chewbaсca and Number

def connvertNumber(n):
    digits = str(n)
    result = []
    for char in digits:
        digit = int(char)
        mod = 9 - digit
        if mod < digit:
            result.append(mod)
        elif mod>digit:
            result.append(digit)
    f_res=int(''.join (map(str,result)))
    return f_res

# print(connvertNumber(27))


def CheckRotation(A:str, B:str):
    C = A + A
    if B in C:
        return True
    else:
        return False
        
# print(CheckRotation("abcd", "qw"))

from collections import Counter
# Creating a Counter from a list
counts = Counter([1, 2, 2, 3, 3, 3])
# print(counts)  # Output: Counter({3: 3, 2: 2, 1: 1})

my_list = [i for i in range(10) if i % 2 == 0]
# print(my_list)


def sortArray(list1):
    for i in range(len(list1)):
        j = 0
        for j in range(j+i, len(list1)):
            if list1[i] > list1[j]:
                c = list1[j]
                list1[j] = list1[i]
                list1[i] = c

    return list1

# print(sortArray([2,0,1]))


def mergedArr(list1,m,list2,n):
    # if len(list1) > m:
    #     for i in range(m):
    #         list1.pop()
    del list1[m: len(list1)]
    del list2[n:len(list2)]
    list1.extend(list2)
    for i in range(m+n):
        for j in range(i+1, m):
            if list1[i] > list1[j]:
                c = list1[j]
                list1[j] = list1[i]
                list1[i] = c
    return list1


print(mergedArr([0],0,[1], 1))
      

      







    

         





