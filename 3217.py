# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        nums_set = set(nums)
        return self._modifiedList(nums_set, head)

    def _modifiedList(self, nums: set[int], head: ListNode | None) -> ListNode | None:
        if head is None:
            return
        if head.val in nums:
            return self._modifiedList(nums, head.next)

        head.next = self._modifiedList(nums, head.next)
        return head
