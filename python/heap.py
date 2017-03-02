#! /usr/bin/env pyth

from Queue import Queue
from copy import deepcopy

class Node:
    def __init__(self, value):
        self.left  = None
        self.right = None
        self.key   = value
        
class Tree:
    def __init__(self):
        self.root = None
    
    def __addNode__(self, value, leaf):
        if value <= leaf.key:
            if leaf.left is not None:
                self.__addNode__(value, leaf.left)
            else:
                leaf.left = Node(value)                
        else:
            if leaf.right is not None:
                self.__addNode__(value, leaf.right)
            else:
                leaf.right = Node(value)
           
    def addNode(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__addNode__(value, self.root)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            nodeAction(node)
            self.inOrder(node.right)
        
    def preOrder(self, node):
        if node is not None:
            nodeAction(node)
            self.preOrder(node.left)
            self.preOrder(node.right)
        
    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            nodeAction(node)
            
    def lookUp(self, value, node=None, parent=None):    
        if value < node.key:
            if node.left is None:
                return None, node
            else:
                return self.lookUp(value, node.left, node)
        elif value > node.key:
            if node.right is None:
                return None, node
            else:
                return self.lookUp(value, node.right, node)                  
        return node, parent
        
    def getDepth(self, node):
        if node is None:
            return 0
        else:
            leftDepth = self.getDepth(node.left)
            rightDepth = self.getDepth(node.right)
            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1
                
    def __findMin__(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def __findMax__(self, node):
        while node.right is not None:
            node = node.right
        return node
                
    def __deleteNode__(self, value, curNode, parent=None):
        node, parent = self.lookUp(value, curNode, parent)
        if node is not None:
            if node.left is None and node.right is None:
                if parent.left.key == value: parent.left = None
                elif parent.right.key == value: parent.right = None
                del node
            elif node.left is None and node.right is not None:
                if parent.left.key == value: 
                    parent.left = node.right
                    del node                    
                elif parent.right.key == value: 
                    parent.right = node.right
                    del node
            elif node.left is not None and node.right is None:
                if parent.right.key == value: 
                    parent.right = node.left
                    del node                    
                elif parent.left.key == value: 
                    parent.left = node.right
                    del node
            else: # target node has children on either side
                l = self.getDepth(node.left)
                r = self.getDepth(node.right)
                tmp = None
                if r > l:                   
                    tmp = self.__findMin__(node.right)
                    node.key = tmp.key   
                    self.__deleteNode__(node.key, node.right, node)
                else:
                    tmp = self.__findMax__(node.left)
                    node.key = tmp.key
                    self.__deleteNode__(node.key, node.left, node)    
            
    def deleteNode(self, value):
        self.__deleteNode__(value, self.root)         
                                                      
        
def nodeAction(node):
    print str(node.key) + " ",        
        
def depthTraversal(tree):
    tree.preOrder(tree.root)
        
def breadthTraversal(tree):
    toTraverse = Queue(maxsize = 0)
    toTraverse.put(tree.root)
    while not toTraverse.empty():
        currentNode = traversal.get()
        nodeAction(currentNode)
        if currentNode.left  is not None: 
            toTraverse.put(currentNode.left)
        if currentNode.right is not None: 
            toTraverse.put(currentNode.right)



def main():
    pass

    
if __name__ == "__main__":
    main()
