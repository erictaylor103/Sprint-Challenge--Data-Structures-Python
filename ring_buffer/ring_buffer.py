class RingBuffer:
    def __init__(self, capacity):
        self.current_index = 0 #create a current index counter so we know ar what index we are currently
        self.capacity = capacity #
        self.buffer = []#create an empty buffer to append the items

    def append(self, item):
        self.item = item
        if len(self.buffer) == self.capacity:
            #set the item to be on the current_index of the buffer list
            #this replaces the item in the current_index for the new item in the buffer list
            self.buffer[self.current_index] = item
            
            print(f"New Item: {item}")
            print(f"Buffer: {self.buffer}")
            print(f"Current Index: {self.current_index} \n")
        
        else:
            self.buffer.append(item)
        self.current_index = (self.current_index + 1) % self.capacity

    def get(self):
        return self.buffer