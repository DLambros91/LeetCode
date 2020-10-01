# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digits = []
        while head:
            digits.insert(0, head.val)
            head = head.next
        return sum([2**i * digits[i] for i in range(len(digits))])
