class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class queue:
    def __init__(self):
        self.Front=None
        self.Rear=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.Front=n
        else:
            self.Rear.next=n
        self.Rear=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.Front==self.Rear:
            self.Front=None
            self.Rear=None
        else:
            self.Front=self.Front.next
        self.item_count-=1   
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.Front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.Rear.item
    def size(self):
        return self.item_count  
q1=queue()
q1.enqueue(30)
q1.enqueue(66)
q1.enqueue(70) 
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())



     

