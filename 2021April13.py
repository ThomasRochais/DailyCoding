import operator
def reverse_polish_computation(lst):
    ops = {'+': (lambda x,y: x+y),
        '-': (lambda x,y: x-y),
        '/': (lambda x,y: x/y),
        '*': (lambda x,y: x*y),
    }
    N = len(lst)
    stack = []
    for i in range(N):
        stack.append(lst[i])
        if isinstance(stack[-1], str):
            stack.append(ops[stack.pop()] (stack.pop(-2), stack.pop()))
    if len(stack) == 1:
        return stack.pop()
    else:
        return "None"

print(reverse_polish_computation([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))
print(reverse_polish_computation([15, 7, '-']))
print(reverse_polish_computation([5, 3, '+']))
print(reverse_polish_computation([3, 4, 5, '*', '-']))