"""Q3. Write a program to check if two strings are a rotation of each other?"""
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    concatenated = str1 + str1
    return str2 in concatenated

str1 = "hello"
str2 = "ohell"
result = are_rotations(str1, str2)
print(result) 
