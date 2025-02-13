class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, value):
        if self.is_empty():
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        if self.tail.value == value:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return

        current = self.head
        while current:
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

    def delete_last(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_first(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" ⇄ ")
            current = current.next
        print("None")

    def display_reverse(self):
        current = self.tail
        while current:
            print(current.value, end=" ⇄ ")
            current = current.prev
        print("None")


