import heapq
import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        gifts_heap = [-gift for gift in gifts]
        heapq.heapify(gifts_heap)

        for _ in range(k):
            max_element = -heapq.heappop(gifts_heap)
            heapq.heappush(gifts_heap, -int(math.sqrt(max_element)))

        number_of_remaining_gifts = -sum(gifts_heap)

        return number_of_remaining_gifts