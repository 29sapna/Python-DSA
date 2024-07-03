from SinglyLL import *
class stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_first(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.delete_at_first()
            self.item_count-=1
        else:
            raise IndexError("stack underflow")
    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("empty stack")
    def size(self):
        return self.item_count
s1=stack()
s1.push(20)
s1.push(39)
s1.push(45)
print("top element",s1.peek())
s1.pop()
print("top element",s1.peek())

