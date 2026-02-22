# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # O(n) traversal solution
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #  curr_node, prev_node = head, None

    #     while curr_node:
    #       # the next node is the one after the current node
    #       # but we want to set the pointer ref to the prev node
    #         next_node = curr_node.next
    #         curr_node.next = prev_node

    #         # now we set the previous node to the current
    #         # and the current to the next
    #         prev_node = curr_node
    #         curr_node = next_node

    #     return prev_node

    # O(1) recursive solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: empty list or only one node
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
