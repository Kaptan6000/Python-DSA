
from sys import stdin


def isBalanced(expression) :
    stack = []
    for i in expression:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack)==0:
                return False
            top = stack.pop()
            if top == '(' and i == ')':
                continue
            else:
                return False
    return len(stack)==0    
                







expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
