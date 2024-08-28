#Without in keyword how to check if a string is a substring of another string

def checkSub(s1, s2):
    if len(s1) > len(s2):
        for i in range(len(s1)-len(s2) + 1):
            is_match = True
            for j in range(len(s2)):
                if s1[i+j] != s2[j]:
                    is_match = False
                    break
            if is_match == True:
                print("1")
                return True
    elif len(s1) < len(s2):
        print("Not substring")
    elif len(s1) == 0:
        print("Not a substring")
                
# checkSub("hello", "ell")
# checkSub("world", "word")
# checkSub("apple", "orange")
# checkSub("", "abc")
# checkSub("openai", "pen")
# checkSub("abc", "")
# checkSub("abcdef", "abc")
# checkSub("testcase", "test")
# checkSub("abcdef", "def")
# checkSub("example", "ple")
# checkSub("HelloWorld", "world")
# checkSub("HelloWorld", "World")
# checkSub("a" * 1000 + "b", "b")
# checkSub("a" * 1000 + "b", "bc")
# checkSub("hello!@#world", "@#")
# checkSub("special^&*characters", "^&")
        
#https://leetcode.com/problems/two-sum/description/
# https://leetcode.com/problems/palindrome-number/submissions/1370890366/
        
#check if one string is a roation of another
        
def checkforRotation(s1,s2 ):
    if len(s1) != len(s2):
        return False
    n1 = s1 + s1
    if len(s1) == len(s2):
        for i in range(len(n1)-len(s2)+1):
            is_match = True
            for j in range(len(s2)):
                if n1[i+j] != s2[j]:
                    is_match = False
                    break
            if is_match:
                return True
            
    return False
        
print(checkforRotation("waterbottle", "erbottlewat"))
# print(checkForRotation("abc", "bca"))  # Expected output: True
# print(checkForRotation("abc", "cab"))  # Expected output: True
# print(checkForRotation("abc", "acb"))  # Expected output: False
# print(checkForRotation("hello", "elloh"))  # Expected output: True
# print(checkForRotation("hello", "hellohello"))  # Expected output: False







