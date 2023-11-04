"""Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression."""
def postfix_to_prefix(expression):
    stack = []
    
    operators = set(['+', '-', '*', '/', '^'])
    
    for char in expression:
        if char not in operators:
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = char + operand1 + operand2
            stack.append(prefix_expression)
    
    return stack.pop()

postfix_expr = "ab+cd-*"
prefix_expr = postfix_to_prefix(postfix_expr)
print(prefix_expr)  
