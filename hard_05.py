import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Put the first node of every list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, i, node = heapq.heappop(heap)

            # Add the smallest node to result
            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
