# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s ,f =head ,head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        sec =s.next
        prev = s.next = None

        while sec :
            tem = sec.next
            sec.next = prev
            prev = sec
            sec = tem

        first,sec = head,prev
        while sec:
            tem1,tem2 = first.next ,sec.next
            first.next = sec
            sec.next = tem1
            first = tem1
            sec = tem2


        