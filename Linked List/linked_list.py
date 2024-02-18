class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Is Empty
    def isEmpty(self):
        return self.head is None
    
    # Insert At The Beginning
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    # Insert At The End
    def insertAtTheBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert In Between
    def insertInBetween(self, data, nodeData):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        current = self.head
        while current.next is not None:
            if current.data == nodeData:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

        else:
            print("Node with this data is not exists")
        
    # Delete Node
                
    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    # Display
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

linked_list.insertAtEnd(1)
linked_list.insertAtEnd(2)
linked_list.insertAtEnd(3)

linked_list.display()  # Output: 1 -> 2 -> 3 -> None

linked_list.insertAtTheBeginning(0)

linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

linked_list.delete(2)

linked_list.insertInBetween(1.5, 1)

linked_list.display()