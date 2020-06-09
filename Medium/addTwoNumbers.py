# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        iterator = head
        carry = 0 
        
        # Iterate while at least one of the lists contains more nodes
        while (l1 != None or l2 != None or carry == 1):
            
            # If there are no more nodes remaining but a carry over bit, set the next value to the carry bit
            if l1 == None and l2 == None:
                iterator.val = carry
                carry = 0
            elif l2 == None: # If there are no more elements left in list 2, add only the carry bit and the elements from list 1
                iterator.val = (l1.val + carry) % 10
                carry = 0 if (l1.val + carry) < 10 else 1
                l1 = l1.next
            elif l1 == None: # If there are no more elements left in list 1, add only the carry bit and the elements from list 2
                iterator.val = (l2.val + carry) % 10
                carry = 0 if (l2.val + carry) < 10 else 1
                l2 = l2.next
            else: # If both lists have elements, add the carry bit and the two current node values 
                iterator.val = (l1.val + l2.val + carry) % 10
                carry = 0 if (l1.val + l2.val + carry) < 10 else 1
                l1 = l1.next
                l2 = l2.next
            # Set the iterator to the next Node in the singly Linked List for the next iteration    
            if (l1 != None or l2 != None or carry == 1):
                iterator.next = ListNode()
                iterator = iterator.next
        
        # Return the Singly Linked-List
        return head
