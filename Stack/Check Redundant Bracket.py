from sys import stdin

def checkRedundantBrackets(expression) :
    s = []
    for i in expression:
        if i == ')':
            top = s[-1]
            s.pop()
            Flag = True
            while top != '(':
                if top == '+' or top == '-' or top == '*' or top == '/':
                    Flag = False
                top = s[-1]
                s.pop()
            if Flag :
                return True    
        else:
            s.append(i)
        
    return False    
            
       




#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
