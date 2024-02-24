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
    def detect(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
l.head=n1
n1.next=n2
n2.next=n1
n2.next=n3
n3.next=n4
n4.next=n1
print(l.detect())
