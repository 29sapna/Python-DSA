class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next!=None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp!=None:
            if temp.data==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp!=None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start!=None:
            self.start=self.start.next 
            if self.start!=None:
                self.start.prev=None
    def delete_last(self):
        if self.start==None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.prev.next=None
    def delete_data(self,data):
        if self.start==None:
            pass
        else:
            temp=self.start
            while temp!=None:
                if temp.data==data:
                    if temp.next!=None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data= self.current.data
        self.current=self.current.next
        return data
mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
for x in mylist:
    print(x,end=' ')
print()







