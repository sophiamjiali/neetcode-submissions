# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Want to find two nodes that store the same node in the next
        # attribute (can do assertion)

        # Naively, O(n^2) runtime to compare each node to all others
        # Redundant because we re-check the full list, how to minimize?

        # Track membership of nodes in a O(n) set, for each node, check 
        # membership in nodes already traversed in O(1)

        seen = set()
        curr = head

        while curr:
            if curr in seen: 
                return True
            seen.add(curr)
            curr = curr.next

        return False