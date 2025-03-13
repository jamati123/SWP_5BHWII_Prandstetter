import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value
    
    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))

if __name__ == "__main__":
    linked_list = LinkedList()
    for _ in range(10):  
        linked_list.append(random.randint(1, 100))
    
    print("Länge der Liste:", len(linked_list))
    print("Elemente der Liste:")
    linked_list.print_list()
    
    print("Iterieren durch die Liste:")
    for value in linked_list:
        print(value, end=" ")
