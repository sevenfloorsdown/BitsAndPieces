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
    tree = Tree()
    tree.addNode(8)
    tree.addNode(3)
    tree.addNode(10)
    tree.addNode(1)
    tree.addNode(6)
    tree.addNode(4)
    tree.addNode(7)
    tree.addNode(14)
    tree.addNode(13)
    tree.addNode(15)
    tree.addNode(9)

    '''
    Our tree should be:
            8
        /       \    
       3        10
      / \      /  \ 
     1   6    9    14
        / \        / \
        4 7      13  15 
    '''
    
    # output should be: 1 3 4 6 7 8 9 10 13 14 15
    print "In-order traversal:"
    tree.inOrder(tree.root) 
    
    # output should be: 8 3 1 6 4 7 10 9 14 13 15
    print "\nPre-order traversal:"
    tree.preOrder(tree.root)
    
    # output should be:  1 4 7 6 3 9 13 15 14 10 8
    print "\nPost-order traversal:"
    tree.postOrder(tree.root)
    
    print "\nDepth-first traversal:"
    depthTraversal(tree)
    
    # output should be: 8 3 10 1 6 9 14 4 7 13 15
    print "\nBreadth-first traversal:"
    breadthTraversal(tree)    
    
    #print "\nLookup:"
    #x = tree.lookUp(32)
    #if x[0] is not None: print "x[0]: " + str(x[0].key)
    #if x[1] is not None: print "x[1]: " + str(x[1].key)
    
    tree2 = deepcopy(tree)
    x = 1 
    tree2.deleteNode(x)
    print "\nBreadth-first traversal after deletion:" + str(x)
    breadthTraversal(tree2)  

    x = 3
    tree2.deleteNode(x)    
    print "\nBreadth-first traversal after deletion:" + str(x)
    breadthTraversal(tree2)   
    
    x = 15
    tree2.deleteNode(x)
    print "\nBreadth-first traversal after deletion:" + str(x)
    breadthTraversal(tree2)  
    x = 14  
    tree2.deleteNode(x)        
    print "\nBreadth-first traversal after deletion:" + str(x)
    breadthTraversal(tree2)       
  
    print "\nNew tree!!!"
    x = 14
    tree3 = deepcopy(tree)
    tree3.deleteNode(x)   
    print "\nBreadth-first traversal after deletion:" + str(x)
    breadthTraversal(tree3)
    
    print "\nDepth-first"
    depthTraversal(tree3)

    
if __name__ == "__main__":
    main()
