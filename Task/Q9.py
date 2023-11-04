"""Q9. Write a program to reverse a stack."""
def reverse_stack(stack):
    if not stack:
        return

    top = stack.pop()
    reverse_stack(stack)
    _insert_at_bottom(stack, top)

def _insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        _insert_at_bottom(stack, item)
        stack.append(top)

stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  
