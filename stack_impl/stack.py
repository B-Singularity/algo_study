from linkedList_impl.linkedList import LinkedList

class Stack:
    def __init__(self):
        self.dll = LinkedList()
        self.size = 0

    def is_empty(self):
        return self.dll.is_empty()

    def push(self, value):
        self.dll.append(value)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.dll.tail.value
        self.dll.delete_last()
        self.size -= 1
        return value

    def peek(self):
        return None if self.is_empty() else self.dll.tail.value

    def get_size(self):
        return self.size

    def display(self):
        self.dll.display_reverse()

stack = Stack()
stack.push(1)
stack.display()
stack.push(3)
stack.display()