class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class SLL:
    def __init__(self):
        self.head=None 
    def merge(self,l1,l2):
        dummy=Node(-199999)
        curr=dummy 
        while l1 and l2:
            if(l1.data<l2.data):
                curr.next=l1
                l1=l1.next 
            else:
                curr.next=l2
                l2=l2.next 
            curr=curr.next 
        if l1:
            curr.next=l1 
        elif l2:
            curr.next=l2 
        return dummy.next
    def display(self):
        temp=self.head 
        while temp:
            print(temp.data,end="-->")
            temp=temp.next 


l1=SLL()
l2=SLL() 
n1=Node(1)
n2=Node(3)
nn1=Node(2)
nn2=Node(4)
l1.head=n1
n1.next=n2 
l2.head=nn1 

nn1.next=nn2 
ml=SLL()
ml.head=ml.merge(l1.head,l2.head)
ml.display()


