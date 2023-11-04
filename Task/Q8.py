"""Q8. Write a program to check if all the brackets are closed in a given code snippet."""
def are_brackets_balanced(code):
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    
    for char in code:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return not stack 

code_snippet = "{[()()]}"
result = are_brackets_balanced(code_snippet)
print(result)  
