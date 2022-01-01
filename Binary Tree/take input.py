class binarytree():
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

# Take input nodes line by line.

def takeinput():
    data = int(input())
    if data==-1:
        return None
    root = binarytree(data)
    root.left = takeinput()
    root.right = takeinput()
    return root
    
root = takeinput()        
        
        
