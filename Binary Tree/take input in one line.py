import queue
class binarytree():
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
        
# Take space separated input in one line.

def takeinput():
    arr = list(map(int,input().split()))
    start = 0 
    root = binarytree(arr[start])
    start += 1 
    q = queue.Queue()
    q.put(root)
    
    while  not q.empty():
        currentnode = q.get()
        
        leftchild = arr[start]
        start += 1 
        if leftchild != -1:
            
            leftNode = binarytree(leftchild)
            currentnode.left =leftNode
            q.put(leftNode)
        
        rightchild = arr[start]
        start += 1 
        if rightchild != -1:
            rightNode = binarytree(rightchild)
            currentnode.right =rightNode
            q.put(rightNode)
    return root 
