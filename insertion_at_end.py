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
            print("empty")
        else:
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print()
    def insertend(self,data):
        temp=self.head
        if temp is None:
            new=Node(data)
            temp=new
        else:
            new=Node(data)
            while temp.next:
                temp=temp.next
            temp.next=new
l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
l.head=n1
n1.next=n2
n2.next=n3
l.insertend(40)
l.display()
