class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        self.head = prev

    def middle(self):
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def ispali(self):
        sh = self.middle()
        shl = SLL()
        shl.head = sh
        shl.reverse()
        fh = self.head
        ss = shl.head
        while fh and ss:
            if fh.data != ss.data:
                return False
            fh = fh.next
            ss = ss.next
        return True

# Create a singly linked list
l = SLL()
n1 = Node(1)
n2 = Node(2)
n3 = Node(5)
l.head = n1
n1.next = n2
n2.next = n3

# Check if the linked list is a palindrome
print(l.ispali())
