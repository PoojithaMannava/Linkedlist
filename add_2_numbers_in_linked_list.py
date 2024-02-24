# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        current = head
        carry = 0
        while (l1 != None or l2 != None or carry != 0):
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + carry
            current.next = ListNode(total % 10)
            carry = total // 10
            # Move list pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return head.next

# Helper function to display linked list
def display_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
# Create linked lists representing numbers 342 and 465
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Create an instance of the Solution class
solution = Solution()

# Call the addTwoNumbers method
result = solution.addTwoNumbers(l1, l2)

# Display the input linked lists and the result
print("Input Linked List 1:")
display_linked_list(l1)

print("\nInput Linked List 2:")
display_linked_list(l2)

print("\nResult Linked List:")
display_linked_list(result)
