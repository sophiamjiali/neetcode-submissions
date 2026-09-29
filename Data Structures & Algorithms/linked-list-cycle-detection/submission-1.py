# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Want to find two nodes that store the same node in the next
        # attribute (can do assertion)

        # Naively, O(n^2) runtime to compare each node to all others.
        # Redundant because we re-check the full list, how to minimize?

        # Tracking previously seen nodes with a set will result in O(n) 
        # space usage, but O(n) runtime.

        # Floyd's cycle detection: use a slow and fast pointer, if there
        # is a cycle, they will overlap in it. Else, the fast pointer will
        # reach the end of the list

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True

        return False