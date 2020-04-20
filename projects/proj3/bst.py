"""
filename: bst.py
author: Gabriel Wallace
A class for a binary search tree.
"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
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

    def delete(self, val):
        if self.root is None:
            return node

        parent = None
        node = self.root

        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right

        if node is None or node.val != val:
            return None

        #Node to remove has no children
        elif node.left is None and node.right is None:
            if val < parent.val:
                parent.left = None
            elif val > parent.val:
                parent.right = None

        #Node to remove only has one child
        elif node.left is None or node.right is None:
            if val < parent.val:
                parent.left = node.left
            elif val > parent.val:
                parent.right = node.right

        #Node has left and right children
        else:
            temp_node = node.right
            temp_node_parent = node
            while temp_node.left:
                temp_node_parent = temp_node
                temp_node = temp_node.left

            node.val = temp_node.val
            if temp_node.right:
                if temp_node_parent.val > temp_node.val:
                    temp_node_parent.left = temp_node.right
                elif temp_node_parent.val < temp_node.val:
                    temp_node_parent.right = temp_node.right
            else:
                if temp_node.val < temp_node_parent.val:
                    temp_node_parent.left = None
                else:
                    temp_node_parent.right = None

    def search(self, val):
        if self.root is not None:
            return self._search(self.root, val)
        else:
            return None
 
    def _search(self, node, val):
        if val == node.val:
            print(node.val)
            return node
        elif val < node.val and node.left is not None:
            print(node.val)
            return self._search(node.left, val)
        elif val > node.val and node.right is not None:
            print(node.val)
            return self._search(node.right, val)
        else:
            print("None")

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        else:
            return max(self._height(node.left), self._height(node.right)) + 1

    def min(self):
        return self._min(self.root).val

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def max(self):
        return self._max(self.root).val

    def _max(self, node):
        while node.right:
            node = node.right
        return node
 
    def printTree(self, traversal_type='inorder'):
        if self.root is not None:
            if traversal_type == 'preorder':
                self._preorder(self.root)
            elif traversal_type == 'postorder':
                self._postorder(self.root)
            else:
                self._inorder(self.root)
    
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(str(node.val) + " ", end='')
            self._inorder(node.right)

    def _preorder(self, node):
        if node is not None:
            print(str(node.val) + " ", end='')
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(str(node.val) + " ", end='')

    def prettyPrint(self, node, level=0):
        print("  "*level + repr(node.val))
        if node.left is not None:
            self.prettyPrint(node.left, level + 1)
        if node.right is not None:
            self.prettyPrint(node.right, level + 1)

if __name__ == "__main__":
    lst = [30, 10, 45, 38, 20, 50, 25, 33, 8, 12]

    tree = Tree()

    for x in lst:
        tree.insert(x)

    tree.printTree()
    print()
    tree.prettyPrint(tree.root)

    print(tree.height())

