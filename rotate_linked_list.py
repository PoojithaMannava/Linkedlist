class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    def rotate(self):
        pass

l=SLL()
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
l.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
