class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def countn(self):
        temp=self.head
        c=0
        while temp:
            c=c+1
            temp=temp.next
        return c
        
l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
l.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
print(l.countn())
