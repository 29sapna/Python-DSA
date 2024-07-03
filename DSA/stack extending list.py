class stack(list): #here list is parent class of stack
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop() #parent class pop method is call here
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("no attribute 'insert' in stack")
s1=stack()
#s1.insert(0,10)
s1.push(2)
s1.push(3)
s1.push(5)
print("top value=",s1.peek())
print()