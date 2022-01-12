class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()
        
        
        
def takeInput():
    print("Enter root data")
    root = int(input())
    if root == -1:
        return None 
    rootNode = TreeNode(root)
    print('Number of child of',root)
    childerncount = int(input())
    for i in range(childerncount):
        child = takeInput()
        rootNode.children.append(child)
    return rootNode
    
    
    
def printTree(root):
    if root == None:
        return 
    print(root.data,end=':')
    for i in root.children:
        print(i.data,end=',')
    print()    
    for i in root.children:
        printTree(i)
        
root = takeInput()
printTree(root)
    
