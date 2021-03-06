class treeItem:
   def __init__(self, value=None):
       self.value = value

   def getValue(self):
       return self.value

class Node:

    def __init__(self, tree, vals=[None, None, None], p=None, links=[None, None, None, None]):
        self.tree = tree
        self.vals = vals
        self.parent = p
        self.links = links

    def destroy(self):
        self.vals = [None, None, None]
        self.parent = None
        self.links = [None, None, None, None]

    def destroyAll(self):
        if self.links[0] == None:
            self.destroy()
        elif self.getSize() == 2:
            for v in self.links[0].inorder():
                v.destroy()
            for v in self.links[2].inorder():
                v.destroy()
            for v in self.links[3].inorder():
                v.destroy()
        else:
            for v in self.links[0].inorder():
                v.destroy() 
            for v in self.links[3].inorder():
                v.destroy()

    def getSize(self):
        size = 0
        for v in self.vals:
            if not v == None:
                size += 1
        return size

    def contains(self, value):
        return value in self.vals

    def inorder(self):
        a = []
        if self.links[0] == None:
            for v in self.vals:
                if not v == None:
                    a.append(v)
        elif self.getSize() == 2:
            for v in self.links[0].inorder():
                a.append(v)
            a.append(self.vals[0])   
            for v in self.links[2].inorder():
                a.append(v)
            a.append(self.vals[2])  
            for v in self.links[3].inorder():
                a.append(v)
        else:
            for v in self.links[0].inorder():
                a.append(v)
            a.append(self.vals[1])  
            for v in self.links[3].inorder():
                a.append(v)
        return a

    def retrieveItem(self, searchKey, treeItem):
        for v in self.vals:
            if v == searchKey:
                treeItem.value = v
                return True
        if self.links[0] == None:
            treeItem.value = None
            return False
        if self.getSize() == 2:
            if searchKey < self.vals[0]:
                return self.links[0].retrieveItem(searchKey, treeItem)
            if searchKey < self.vals[2]:
                return self.links[2].retrieveItem(searchKey, treeItem)
            return self.links[3].retrieveItem(searchKey, treeItem)
        if searchKey < self.vals[1]:
            return self.links[0].retrieveItem(searchKey, treeItem)
        return self.links[3].retrieveItem(searchKey, treeItem)

    def insertItem(self, item):
        if self.getSize() == 0:                                 # If the node of self has 0 elements.
            self.vals = [None, item, None]
            return
        elif self.contains(item):
            return                                              # If self contains the item, stop inserting.
        elif self.links == [None, None, None, None]:                             # If self is a leaf.  
            self.insertInNode(item)
            return  
        elif self.getSize() == 2:                               # If the node of self has 2 elements.
            if item < self.vals[0]:
                self.links[0].insertItem(item) 
            elif item < self.vals[2]:
                self.links[2].insertItem(item)
            else:
                self.links[3].insertItem(item)
            return
        if item < self.vals[1]:                                 # If the node of self has 1 element.
            self.links[0].insertItem(item)
            return
        self.links[3].insertItem(item)  

    def insertInNode(self, item):
        if self.getSize() == 0:
            self.vals = [None, item, None]    
        elif self.getSize() == 1: 
            middle = self.vals[1]
            if item < middle:
                self.vals = [item, None, middle]
                return
            self.vals = [middle, None, item]
        elif self.getSize() == 2:
            small, large = self.vals[0], self.vals[2]                  
            if item < small:
                self.vals[0], self.vals[1] = item, small
            elif item < large:
                self.vals[1] = item
            elif item > large:
                self.vals[1], self.vals[2] = large, item
            self.split()

    def split(self):
        isLeaf = False
        if self.links[0] == None:
            isLeaf = True

        small = self.vals[0]
        middle = self.vals[1]
        large = self.vals[2]
        self.vals = [None, small, None]

        n1 = self
        n2 = Node(self.tree, [None, large, None])

        if self.parent == None:					# If self has no parent.
            p = Node(self.tree, [None, None, None], None, [n1, None, None, n2])
        else:							# If self has a parent.
            p = self.parent
            if p.getSize() == 1:
                if middle < p.vals[1]:
                    p.links[0] = n1 
                    p.links[2] = n2
                else:
                    p.links[2] = n1 
                    p.links[3] = n2
            else:
                if middle < p.vals[0]:
                    p.links[0] = n1
                    p.links[1] = n2
                elif middle < p.vals[2]:
                    p.links[1] = n1
                    p.links[2] = n2
                else:
                    midNode = p.links[2]
                    p.links[1] = midNode
                    p.links[2] = n1
                    p.links[3] = n2

        # Rearranging links
        n1.parent = p
        n2.parent = p

        if not self.tree.root.parent == None:
            self.tree.height += 1
            self.tree.root = self.tree.root.parent

        if not isLeaf:                       # If self is not a leaf
            small = n1.links[0]
            smid = n1.links[1]
            mid = n1.links[2]
            large = n1.links[3]
            n1.links = [small, None, None, smid]
            n2.links = [mid, None, None, large]
            mid.parent, large.parent = n2, n2
            small.parent, smid.parent = n1, n1
        p.insertInNode(middle) 

    def getNode(self, searchKey):
        for i in range(3):
            if self.vals[i] == searchKey:
                return (self, i)
        if self.links[0] == None:
            return (None, 0)
        if self.getSize() == 2:
            if searchKey < self.vals[0]:
                return self.links[0].getNode(searchKey)
            if searchKey < self.vals[2]:
                return self.links[2].getNode(searchKey)
            return self.links[3].getNode(searchKey)
        if searchKey < self.vals[1]:
            return self.links[0].getNode(searchKey)
        return self.links[3].getNode(searchKey)      

    def getSuccesor(self, searchKey):
        if self.links[0] == None:
            for i in range(3):
                if not self.vals[i] == None and self.vals[i] > searchKey:
                    return (self, i)
        elif self.getSize() == 2:
            if searchKey < self.vals[2]:
                if not self.links[2].vals[0] == None:
                    return (self.links[2], 0)
                return (self.links[2], 1)
            if not self.links[3].vals[0] == None:
                return (self.links[3], 0)
            return (self.links[3], 1)
        else:
            if not self.links[3].vals[0] == None:
                return (self.links[3], 0)
            return (self.links[3], 1)
        return (None, 0)


    def deleteItem(self, searchKey):
        n = self.getNode(searchKey)                     # n[0] = node, n[1] = i where n[0].vals[i] == searchKey. 
        s = (None, 0)
        leafNode = n[0]
        if not n[0] == None:                            # If dataItem is found
            if not n[0].links[0] == None:               # If dataItem is not in a leaf
                s = n[0].getSuccesor(searchKey)
                temp = n[0].vals[n[1]]                  # Swap dataitem with inorder successor
                n[0].vals[n[1]] = s[0].vals[s[1]]       
                s[0].vals[s[1]] = temp
                leafNode = s[0]
                                                        # Removal begins here                            
            if leafNode.getSize() == 1:
                leafNode.vals = [None, None, None]
                leafNode.fix()
            else:
                if n[1] == 0:
                    large = leafNode.vals[2]
                    leafNode.vals = [None, large, None]
                else:
                    small = leafNode.vals[0]
                    leafNode.vals = [None, small, None]
            return True
        return False

    def fix(self):
        if self.parent == None:                         # If self is the root.
            if not self.links[0] == None:
                self.tree.root = self.links[0]
                self.links[0].parent = None      
            elif not self.links[3] == None:
                self.tree.root = self.links[3]
                self.links[3].parent = None
            newheight = self.tree.height - 1
            if newheight > 0:
                self.tree.height = newheight
            else:
                self.tree.height = 1
            self.destroy()
        else:
            p = self.parent                             # If self has a parent 
            i = 0
            rd = False
            for l in p.links:
                if not l == None and not l == self and l.getSize() == 2:
                    self.redistribute(l, i)
                    rd = True
                    break
                i+=1
            if not rd:
                j = 0
                for l in p.links:
                    if l == self:
                        break
                    j+=1
                if j == 0:                            # If self is the left node.
                    if not p.links[2] == None:
                        self.merge(p.links[2], 2)
                    else:   
                        self.merge(p.links[3], 3)
                elif j == 2:                            # If self is the middle node.
                    self.merge(p.links[0], 0)
                else:                                 # If self is the right node.
                    if not p.links[2] == None:
                        self.merge(p.links[2], 2)
                    else:
                        self.merge(p.links[0], 0)
               
    def merge(self, adjecent, adjlink):
        p = self.parent
        p_item = 0
        if p.getSize() == 1:
            p_item = p.vals[1]
            p.vals[1] = None
            if adjlink == 0:
                adjecent.vals = [adjecent.vals[1], None, p_item]
                p.links[3] = None
            else:
                adjecent.vals = [p_item, None, adjecent.vals[1]]
                p.links[0] = None
        else:
            if adjlink == 0:                   # If adjecent is the left node/self is the middle node.
                p_item = p.vals[0]
                p.vals = [None, p.vals[2], None]
                p.links[2] = None
                adjecent.vals = [adjecent.vals[1], None, p_item]
            elif adjlink == 2:                   # If adjecent is the middle node.
                if p.links[0].vals == [None, None, None]:   # If self is the left node.
                    p_item = p.vals[0]
                    p.vals = [None, p.vals[2], None]
                    p.links[0] = p.links[2]
                    p.links[2] = None    
                    adjecent.vals = [p_item, None, adjecent.vals[1]]
                else:                                       # Self is the right node.
                    p_item = p.vals[2]  
                    p.vals = [None, p.vals[0], None]    
                    p.links[3] = p.links[2]
                    p.links[2] = None    
                    adjecent.vals = [adjecent.vals[1], None, p_item]
            else:                             # If adjecent is the right node.
                p_item = p.vals[2]
                p.vals = [None, p.vals[0], None]
                p.links[2] = None
                adjecent.vals = [p_item, None, adjecent.vals[1]] 
        if not self.links == [None, None, None, None]:              # If n is internal
            child = None
            for l in self.links:
                if not l == None:
                    child = l
                    break
            if ((not adjecent.links[0].vals[0] == None and adjecent.links[0].vals[0] > child.vals[2])
               or (not adjecent.links[0].vals[1] == None and adjecent.links[0].vals[1] > child.vals[2])):
                small = adjecent.links[0]
                adjecent.links[2] = small
                if not child.links[0] == None:
                    child.parent = adjecent
                    adjecent.links[0] = child
                else:
                    child.parent = adjecent
                    adjecent.links[0] = child
            else:
                large = adjecent.links[3]
                adjecent.links[2] = large
                if not child.links[0] == None:
                    child.parent = adjecent
                    adjecent.links[3] = child
                else:
                    child.parent = adjecent
                    adjecent.links[3] = child 
        self.destroy()
        if adjecent.parent.vals == [None, None, None]:
            adjecent.parent.fix()            

    def redistribute(self, sibling, siblink):       
        p, p_change, sib_vals = self.parent, None, [sibling.vals[0], sibling.vals[1], sibling.vals[2]]

        if p.getSize() == 1:                            # If parent has 1 element.
            p_change = p.vals[1]
            if siblink == 0:
                p.vals[1] = sib_vals[2]
                sibling.vals = [None, sib_vals[0], None]
            else:
                p.vals[1] = sib_vals[0]
                sibling.vals = [None, sib_vals[1], None]   
            self.vals = [None, p_change, None]
        else:                                           # If parent has 2 elements.
            if siblink == 0:
                p_change = p.vals[0]
                p.vals[0] = sib_vals[2]
                self.vals[1] = p_change
                sibling.vals = [None, sib_vals[0], None]
            elif siblink == 2:
                if p.links[0].vals == [None, None, None]:
                    p_change = p.vals[0]
                    p.vals[0] = sib_vals[0]
                    self.vals[1] = p_change
                    sibling.vals = [None, sib_vals[2], None]
                else:
                    p_change = p.vals[2]
                    p.vals[2] = sib_vals[2]
                    self.vals[1] = p_change
                    sibling.vals = [None, sib_vals[0], None]
            else:
                p_change = p.vals[2]
                p.vals[2] = sib_vals[0]
                self.vals[1] = p_change
                sibling.vals = [None, sib_vals[2], None]        
                
        if not self.links == [None, None, None, None]:       # If self is an internal node.
            i = 0
            child = None
            sib_children = [sibling.links[0], sibling.links[2], sibling.links[3]]
            for l in self.links:
                if not l == None:
                    child = l
                    break
                i+=1
            if siblink == 0:                                 # If sib is the right node/self is the middle node.
                        sibling.links[2], sibling.links[3] = None, sib_children[1]
                        self.links[0] = sib_children[2]
            if siblink == 2:                                 # If sib is the middle node.                            
                        if p.links[0] == self:               # If self is the left node.
                            sibling.links[0], sibling.links[2] = sib_children[1], None
                            self.links[3] = sib_children[0]            
                        else:                                # If self is the right node.
                            sibling.links[3], sibling.links[2] = sib_children[1], None
                            self.links[0] = sib_children[2]  
            else:                                            # If sib is the right node/self is the middle node.
                sibling.links[0], sibling.links[2] = sib_children[1], None
                self.links[3] = sib_children[0]   


class TwoThreeTree:

    def __init__(self):
        self.root = Node(self)
        self.height = 1

    def createTree(self):
        pass

    def destroyTree(self):
        self.root.destroyAll()

    def treeIsEmpty(self):
        if self.root.vals == [None, None, None]:
            return True
        return False

    def treeLength(self):
        if self.treeIsEmpty():
            return 0
        return self.height

    def insertItem(self, newItem):
        self.root.insertItem(newItem)

    def deleteItem(self, searchKey):
        self.root.deleteItem(searchKey)

    def retrieveItem(self, searchKey, treeItem):
        return self.root.retrieveItem(searchKey, treeItem)

    def traverse(self):
        return self.root.inorder()



