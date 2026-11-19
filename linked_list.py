class Node:
    def __init__(self, value): # constructor method
        self.value = value # self similar to 'this' in Java although could replace self with another keyword as long it's changed in parameter list
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value, index=None):
        
        new_node = Node(value)
        
        if index is None:
            if not self.head: # if head is empty, put new_node there
                self.head = new_node
                return True
            
            current = self.head
            while current.next: # if head not empty, go through list to find end
                current = current.next
            current.next = new_node
            return True
        
        if index == 0:
            new_node.next = self.head # set after new_node to point to head
            self.head = new_node # set head to new_node
            return True
        
        if index < 0:
            print("Error: Index negative.")
            return False
        
        current = self.head
        current_index = 0
        
        while current and current_index < (index - 1):
            current = current.next
            current_index += 1
        if not current: # if while loop made current be None
            print(f"Error: Index {index} out of bounds.")
            return False
        
        new_node.next = current.next
        current.next = new_node
        return True
    
    def delete(self, value): # remove first occurence only
        
        if not self.head: # nothing to delete
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
            
        if current.next:
            current.next = current.next.next
            return True
        return False
    
    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return values