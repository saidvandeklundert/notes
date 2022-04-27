# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_str = ""

        while head:
            addition = head.val
            bin_str += str(addition)

            head = head.next

        print(bin_str)
        return_value = int(bin_str, 2)
        print(return_value)

        return return_value
