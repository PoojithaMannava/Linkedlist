class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def middle(self):
        slow=fast=self.head
        while fast and fast.next:#fast.next is used to handel both odd and even number of nodes
            slow=slow.next
            fast=fast.next.next
        return slow.data
        
    
l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
l.head=n1
n1.next=n2
n2.next=n3
print(l.middle())
        
