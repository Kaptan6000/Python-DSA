
from sys import stdin

def countBracketReversals(inputString) :
    if len(inputString)%2!= 0:
        return -1
    else:
        s = []
        for i in inputString:
            if i == '{':
                s.append(i)
            elif i == '}' and len(s)==0:
                s.append(i)
            elif i == '}' and len(s)!=0 and s[-1]=="{":
                s.pop()
            elif i == '}' and len(s)!=0 and s[-1] != '{':
                s.append(i)
        c = 0
        while len(s)!=0:
            c1 = s.pop()
            c2 = s.pop()
            if c1==c2:
                c += 1
            elif c1=='{' and c2 =='}':
                c += 2
        return c        
    
    
    

#main
print(countBracketReversals(stdin.readline().strip()))
