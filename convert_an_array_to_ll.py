class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
def printl(head):
    while head:
        print(head.data,end=" ")
        head=head.next
def arll(
    a):
    head=Node(a[0])
    temp=head 
    for i in range(1,len(a)):
        temp.next=Node(a[i])
        temp=temp.next 
    return head 
a=[4,5,6,7]
m=arll(a)
printl(m)



        
