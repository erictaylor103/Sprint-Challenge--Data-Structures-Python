import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#create a BST class

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self is None:
            #if there is no root node, set the value to the node
            self = BSTNode(value)
        else:
            #if the new value is less than the value, then go left
            if value < self.value:
                #check if the node to the left is not empty
                if self.left is not None:
                    #if not empty, insert the new value
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)

            else:
                    #if the left node is not empty, set it to the node (new value)
                if self.right is not None:
                    #if not empty, insert the new value
                    self.right.insert(value)
                else:
                    #if empty, set the right node to the new value
                    self.right = BSTNode(value)

    
    def contains(self, target):
        #if there is no node, return false
        if self is None:
            return False
        if target == self.value:
            return True
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
    

# Replace the nested for loops below with your improvements
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)

node = BSTNode(names_1[0])
def findDuplicates():
        for name in names_1:
            node.insert(name)
        for name in names_2:
            if node.contains(name):
                duplicates.append(name)
        return duplicates

findDuplicates()



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
