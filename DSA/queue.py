class queue:
    def __init__(self):
        self.items=[]
        # self.front=None
        # self.rear=None
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):        #it add the elemnt at last
        self.items.append(data)
    def dequeue(self): #it delete the element in first
        if not self.is_empty():
            self.items.pop(0) 
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Overflow")
    def get_rear(self):
          if not self.is_empty():
            return self.items[-1]
          else:
               raise IndexError("Queue Overflow")
    def size(self):
        return len(self.items)
q1=queue()
try:
     print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Front=",q1.get_front(),"Rear=",q1.get_rear())
try:
    q1.dequeue()
    print("Queue has now",q1.size(),"elements")
except IndexError as e:
    print(e.args[0])
