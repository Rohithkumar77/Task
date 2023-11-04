"""Q4. Write a program to print the first non-repeated character from a string?"""
def first_non_repeated_character(string):
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string:
        if char_count[char] == 1:
            return char

    return None

string = "programming"
result = first_non_repeated_character(string)
print(result) 
