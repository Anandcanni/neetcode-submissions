"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        c = head
        old_new = {}
        while c:
            node = Node(x=c.val)
            old_new[c] = node
            c = c.next
        c = head
        while c:
            new_node = old_new[c]
            new_node.next = old_new[c.next] if c.next else None
            new_node.random = old_new[c.random] if c.random else None
            c = c.next
        return old_new[head]