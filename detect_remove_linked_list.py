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
        print()

    def detect_and_remove_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # If there is no cycle
        if not fast or not fast.next:
            return

        # Reset pointers to remove the cycle
        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

# Create the linked list with a cycle
l = SLL()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
l.head = n1
n1.next = n2
n2.next = n3
n3.next = n2

# Detect and remove the cycle
l.detect_and_remove_cycle()

# Display the linked list after removing the cycle
l.display()
