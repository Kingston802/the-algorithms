class Node:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        """ Returns the size of the linked list """
        size = 0
        val = self.head 

        while val is not None:
            size+=1
            val = val.pointer

        return size

    def empty(self):
        """ Returns true if linked list is empty """
        if self.head is None:
            return True
        else:
            return False

    def value_at(self, index):
        """ Returns the value at a given index of linked list, returns False if value does not exist"""
        if index > self.size()-1:
            return False

        node = self.head
        for i in range(index):
            node = node.pointer

        return node.value

    def push_front(self, value):
        """ Adds value to the front of linked list """
        newNode = Node(value)
        newNode.pointer = self.head
        self.head = newNode

    def pop_front(self):
        """ Removes value from the front of linked list """
        poppedValue = self.head.value
        self.head = self.head.pointer

        return poppedValue

    def front(self):
        """ Returns value at the front of linked list """
        return self.head.value

    def back(self):
        """ Returns value at the end of linked list """
        node = self.head
        while node.pointer is not None:
            node = node.pointer

        return node.value

    def insert(self, index, value):
        """ Inserts node at given index with given value and returns false if index is not reachable """
        if index > self.size()-1:
            return False

        node = self.head
        for i in range(index-1):
            node = node.pointer

        newNode = Node(value)
        newNode.pointer = node.pointer
        node.pointer = newNode

    def erase(self, index):
        """ Removes node from a given index """
        if index > self.size()-1:
            return False

        node = self.head
        for i in range(index-1):
            node = node.pointer

        node.pointer = node.pointer.pointer 

    def value_n_from_end(self, n):
        """ Returns value n from the end e.g. n=2, for a size of 3 returns value at index 2 """
        node = self.head
        for i in range(self.size()-n-1):
            node = node.pointer

        return node.value

    def reverse(self):
        """ Reverses the linked list """
        prev = None
        current = self.head

        while current is not None:
            next = current.pointer
            current.pointer = prev
            prev = current 
            current = next
        self.head = prev

    def remove_value(self, value):
        """ Removes a given value """ 
        node = self.head

        if node.value == value:
            self.pop_front()

        while node.pointer is not None:
            if node.pointer.value == value:
                break
            node = node.pointer 

# Usage Example
l = LinkedList()

print(l.empty()) # true

n = Node(42)
l.head = n
    
print(l.empty()) # false 

# add two more nodes
n2 = Node(69)
n.pointer = n2
n3 = Node(43)
n2.pointer = n3

print(l.size()) # 3 

print(l.value_at(2)) # 43, zero-indexed

l.push_front(420)
print(l.front()) # 420

l.pop_front()
print(l.front()) # 42

print(l.back()) # 43

l.insert(1, 52) # inserts 52 at index 1

print() # print out contents of linked list 
val = l.head
while val is not None:
    print(val.value)
    val = val.pointer

l.erase(1) # removes 52 from index 1

print() # print out contents of linked list 
val = l.head
while val is not None:
    print(val.value)
    val = val.pointer

print()

print(l.value_n_from_end(1))

l.remove_value(42)

print() # print out contents of linked list 
val = l.head
while val is not None:
    print(val.value)
    val = val.pointer

l.reverse()

print() # print out contents of linked list 
val = l.head
while val is not None:
    print(val.value)
    val = val.pointer


