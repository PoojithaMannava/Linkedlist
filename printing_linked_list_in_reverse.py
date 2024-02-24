class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    def displayr(self):
        st=[]
        temp=self.head
        while temp:
            st.append(temp.data)
            temp=temp.next
        while st:
            print(st.pop(),end=" ")
        


l=SLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
l.head=n1
n1.next=n2
n2.next=n3
l.displayr()

