from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True
        
        node = head
        # convert List
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # is palindrom?
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

a = Solution()
head = [1, 2, 2, 1]
print(a.isPalindrome(head))