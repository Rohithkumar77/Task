"""Q7. Write a program to convert prefix expression to infix expression."""
def is_operator(char):
    return char in '+-*/^'

def prefix_to_infix(expression):
    stack = []
    for char in reversed(expression):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = f'({operand1}{char}{operand2})'
            stack.append(infix_expression)
    
    return stack.pop()

prefix_expr = "*+ab-cd"
infix_expr = prefix_to_infix(prefix_expr)
print(infix_expr)  