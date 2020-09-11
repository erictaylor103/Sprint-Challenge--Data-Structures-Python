class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    #def reverse_list(self, node, prev, current):
    #    self.node = node
    #    self.prev = prev
    #    self.current = self.head
        
    #    while(current is not None):
    #        next = current.next
    #        current.next = prev
    #        prev = current
    #        current = next
    #    self.head = prev

    def reverse_list(self, node, prev):
        self.node = node
        self.prev = prev
        #check if there are no items in the list
        if self.head is None:
            #if there are not items in the list, return None and quit the function
            return
        
        if node.next_node is None:
            self.head = node
            node.next_node = prev
            return
        
        next = node.next_node
        node.next_node = prev

        self.reverse_list(next, node)

