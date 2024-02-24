class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    def remov(self):
        temp=self.head
        while temp and temp.next:
            nex=temp.next
            while nex and temp.data==nex.data:
                temp.next=nex.next
                nex=nex.next
            temp=temp.next
            return temp
l = SLL()
n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(3)
l.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

l.remov()
l.display()
