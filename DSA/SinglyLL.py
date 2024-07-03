class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        return self.start==None
    def insert_at_first(self,data):
        n=Node(data, self.start)
        self.start=n    
    def insert_at_last(self,data):
        n=Node(data)
        if not self.isempty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.data==data:
                return temp
            temp=temp.next
            return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data, temp.next)
            temp.next=n 
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end='')
            temp=temp.next
    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is not None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
                temp.next=None 
    def delete_data(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.data==data:
                self.start=None
            else:
                while temp.next is not None:
                    if temp.next.data==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

# class SSLIterable:
#     def __init__(self,start):
#         self.current=start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if not self.current:
#             raise stop iterator
#             data=self.current.item
#             self.current=self.current.iterator
#             return data 
# mylist=SLL()
# mylist.insert_first(10)
# mylist.insert_first(20)
# mylist.insert_last(30)
# print()
# for x in mylist:
#     print(x, end="")
# print()

def evaluate_post(exp):
    stack=[]
    oper=['+','-','/','*']
    for i in exp:
        if i not in oper:
            stack.append(i)
        else:
            op2=stack.pop()
            op1=stack.pop()
            res=op1+i+op2
            stack.append(res)
    print(stack.pop())

exp=input()
evaluate_post(exp)
