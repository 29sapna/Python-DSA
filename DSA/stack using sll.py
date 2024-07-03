from SinglyLL import *
class stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_first(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty:
            self.mylist.delete_at_first()
            self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.data
    def size(self):
        return self.item_count
s=stack()
s.push(1)
s.push(2)
s.push(3)
print("top element=",s.peek())
print()