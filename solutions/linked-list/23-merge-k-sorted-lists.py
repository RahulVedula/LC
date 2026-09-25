# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        sorted_values = head
        heap = []

        for i, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(heap, (linked_list.val, i))

        while heap:
            val, index = heapq.heappop(heap)
            print(val, index)
            sorted_values.next = lists[index]
            
            if lists[index].next:
                lists[index] = lists[index].next 
                heapq.heappush(heap, (lists[index].val, index))

            sorted_values = sorted_values.next
        
        return head.next
        




        