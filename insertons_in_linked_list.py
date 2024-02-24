class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        if temp is None:
            print("Empty")
        else:
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
    def insert(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
n1=Node(10)
n2=Node(20)
n3=Node(30)
l=SLL()
l.head=n1
n1.next=n2
n2.next=n3
n3.next=None
l.insert(40)
l.display()
