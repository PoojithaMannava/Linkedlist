class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def identical(self, l1, l2):
        while l1 is not None and l2 is not None:
            if l1.data != l2.data:
                return False
            l1 = l1.next
            l2 = l2.next

        # Check if both lists are of the same length
        return l1 is None and l2 is None


# Creating linked lists
l1 = SLL()
l2 = SLL()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
nn1 = Node(10)
nn2 = Node(20)
nn3 = Node(30)
l1.head = n1
n1.next = n2
n2.next = n3
l2.head = nn1
nn1.next = nn2
nn2.next = nn3

# Create an instance of SLL
ml = SLL()

# Check if the linked lists are identical
print(ml.identical(l1.head, l2.head))
