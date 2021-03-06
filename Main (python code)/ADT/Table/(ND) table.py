from binarytree import *
from double_linked_chain import *
from hashmap import *
from redblack_tree import *
from tree_234 import *
from TwoThreeTree import * 


class Table:

    def __init__(self):
        self.implementation = "binaryTree"
        self.pointer = None
        
    def setImplementation(implementation):
        self.implementation = implementation

    def createTable(self):
        if self.implementation = "binaryTree":
            self.pointer = binaryTree()
        elif self.implementation = "doublyLinkedChain":
            self.pointer = Doubly_linked_chain()
        elif self.implementation = "hashmap":
            self.pointer = Hashmap()
        elif self.implementation = "redBlackTree":
            self.pointer = Redblacktree()
        elif self.implementation = "234Tree":
            self.pointer = Tree234()
        elif self.implementation = "23Tree":
            self.pointer = TwoThreeTree()

    def destroyTable(self):
        if self.implementation = "binaryTree":
            self.pointer.clear()
        elif self.implementation = "doublyLinkedChain":
            self.pointer.clear()
        elif self.implementation = "hashmap":
            self.pointer.destroy()
        elif self.implementation = "redBlackTree":
            self.pointer.destroyTree()
        elif self.implementation = "234Tree":
            self.pointer.destroyTree()
        elif self.implementation = "23Tree":
            self.pointer.destroyTree()

    def tableIsEmpty(self):
        if self.implementation = "binaryTree":
            self.pointer.isEmpty()
        elif self.implementation = "doublyLinkedChain":
            self.pointer.isEmpty()
        elif self.implementation = "hashmap":
            return self.pointer.isEmpty()
        elif self.implementation = "redBlackTree":
            return self.pointer.
        elif self.implementation = "234Tree":
            self.pointer.
        elif self.implementation = "23Tree":
            self.pointer.

    def tableLength(self):
        if self.implementation = "binaryTree":
            return len(self.pointer.inorder)
        elif self.implementation = "doublyLinkedChain":
            return len(self.traverseTable())
        elif self.implementation = "hashmap":
            return self.pointer.getLength()
        elif self.implementation = "redBlackTree":
            return self.pointer.
        elif self.implementation = "234Tree":
            self.pointer.
        elif self.implementation = "23Tree":
            self.pointer.

    def tableInsert(newItem):
        if (self.implementation = "doublyLinkedChain" or
            self.implementation = "hashmap"):
            return self.pointer.insert(None, newItem)
        return self.pointer.insert(newItem)

    def tableDelete(self, searchKey):
        if self.implementation = "binaryTree":
            return self.pointer.remove(searchKey)
        elif self.implementation = "doublyLinkedChain":
            return self.pointer.remove(searchKey)
        elif self.implementation = "hashmap":
            return self.pointer.remove(searchKey)
        elif self.implementation = "redBlackTree":
            return self.pointer.
        elif self.implementation = "234Tree":
            self.pointer.
        elif self.implementation = "23Tree":
            self.pointer.

    def tableRetrieve(self, searchKey):
        if self.implementation = "binaryTree":
            return self.pointer.getData(searchKey)
        elif self.implementation = "doublyLinkedChain":
            return self.pointer.getItem(searchKey)
        elif self.implementation = "hashmap":
            return self.pointer.getItem(searchKey)
        elif self.implementation = "redBlackTree":
            return self.pointer.
        elif self.implementation = "234Tree":
            self.pointer.
        elif self.implementation = "23Tree":
            self.pointer.

    def traverseTable(self):
        if self.implementation = "binaryTree":
            return self.pointer.inorder()
        elif self.implementation = "doublyLinkedChain":
            return self.pointer.getTraverse()
        elif self.implementation = "hashmap":
            return self.pointer.traverse()
        elif self.implementation = "redBlackTree":
            return self.pointer.
        elif self.implementation = "234Tree":
            self.pointer.
        elif self.implementation = "23Tree":
            self.pointer.


