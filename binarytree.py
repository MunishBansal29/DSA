#binary tree
from logging import root
import sys

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.dataValue = value
        self.left = left
        self.right = right

# class BinaryTree:
#     def __init__(self):
#         root = None

#     def printTree(self):
#         root = self.root


#tree = BinaryTree()
rootNode = TreeNode('Drinks')
node1 = TreeNode('Cold')
node2 = TreeNode('Hot')

#tree.root = rootNode
rootNode.left = node1
rootNode.right= node2

node3 = TreeNode("Soft Drink")
node4 = TreeNode("Tea")
node5 = TreeNode("Hot milk")

node1.left = node3
node2.right = node4
node2.left = node5

print(rootNode.left.dataValue)

#Height of a tree - max length to a leaf node

height = 0

def treeHeight(T):
    # Implement your solution here
    left_height = 0
    right_height = 0
    global height
    if T.left:        
        left_height = treeHeight(T.left)
        left_height += 1
    if T.right:        
        right_height = treeHeight(T.right)
        right_height += 1

    return max(left_height, right_height)
    # if T.left or T.right:
    #     return max(left_height, right_height)
    # else:
    #     return height
    # pass

print(treeHeight(rootNode)) #2

##Binary tree
class BST():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insertNode(rootNode, value):
    if rootNode.data == None: #i.e. root node is empty
        rootNode.data = value
    elif rootNode.data >= value:
        if rootNode.left is None:
            rootNode.left = BST(value)
        else:
            insertNode(rootNode.left, value)
    else:
        if rootNode.right is None:
            rootNode.right = BST(value) 
        else:
            insertNode(rootNode.right, value)

    return "Node has been successfully inserted !"

def preOrderTraverse(rootNode): #root -> left -> right
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraverse(rootNode.left)
    preOrderTraverse(rootNode.right)


def inOrderTraverse(rootNode): #left->root->right
    if rootNode is None:
        return    
    inOrderTraverse(rootNode.left)
    print(rootNode.data)
    inOrderTraverse(rootNode.right)

def postOrderTraverse(rootNode): #left->right->root
    if rootNode is None:
        return    
    postOrderTraverse(rootNode.left)
    postOrderTraverse(rootNode.right)
    print(rootNode.data)

# def levelOrderTraverse(rootNode): #print all the nodes which are the same level at the same time
#     if rootNode is None:
#         return    
#     postOrderTraverse(rootNode.left)
#     postOrderTraverse(rootNode.right)
#     print(rootNode.data) 

rootNode = BST(100)
insertNode(rootNode, 110)
insertNode(rootNode, 55)
insertNode(rootNode, 77)
insertNode(rootNode, 78)
insertNode(rootNode, 200)
insertNode(rootNode, 44)
insertNode(rootNode, 205)
insertNode(rootNode, 198)

preOrderTraverse(rootNode)
print("------------------")
inOrderTraverse(rootNode)


#Count the number of visible nodes in Binary Tree
class BSTNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None

rootNode = BSTNode(5)
node1 = BSTNode(3)
node2 = BSTNode(10)
node3 = BSTNode(20)
node4 = BSTNode(21)
node5 = BSTNode(1)

rootNode.left = node1
rootNode.right = node2
node1.left = node3
node1.right = node4
node2.left = node5

preOrderTraverse(rootNode)

count = 0
def visibleNodeCount(root, maxvalue):
    global count
    if root is None:
        return

    if root.data >= maxvalue:
        count += 1
        maxvalue = max(maxvalue, root.data)

    visibleNodeCount(root.left, maxvalue)
    visibleNodeCount(root.right, maxvalue)
    
    return count

maxvalue = -sys.maxsize-1 #negative max value so that root is always greater than this value

print("Visible node count= ", visibleNodeCount(rootNode, maxvalue))



