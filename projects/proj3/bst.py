"""
filename: bst.py
author: Gabriel Wallace
A class for a binary search tree.
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    def getVal(self):
        return self.val
    
    def setVal(self,newval):
        self.val = newval
        
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def setLeft(self,newleft):
        self.left = newleft
        
    def setRight(self,newright):
        self.right = newright
        
class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
        
    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)
 
    def find(self, val):
        return self._find(self.root, val)
 
    def _find(self, node, val):
        if node is None:
            return None
        elif val == node.val:
            return node
        elif val < node.val and node.left is not None:
            print(node.val)
            return self._find(node.left, val)
        elif val > node.val and node.right is not None:
            print(node.val)
            return self._find(node.right, val)
 
    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)
    
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            #print(str(node.val) + " ", end='')
            print(node.val)
            self._inorder(node.right)


if __name__ == "__main__":
    lst = [30, 10, 45, 38, 20, 50, 25, 33, 8, 12]

    tree = Tree()

    for x in lst:
        tree.insert(x)

    tree.inorder()
    print()
    print(tree.find(38).val)

