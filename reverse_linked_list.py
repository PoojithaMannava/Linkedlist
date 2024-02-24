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
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        self.head=prev
        return self.head

l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
l.head=n1
n1.next=n2
n2.next=n3
l.reverse()
l.display()
