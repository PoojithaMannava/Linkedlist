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
    def eveo(self):
        odd=self.head
        even=self.head.next
        temp=even
        while(even and even.next):
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=temp
        return odd

l=SLL()
n1=Node(2)
n2=Node(1)
n3=Node(3)
n4=Node(5)
l.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
l.eveo()
l.display()
