from collections import deque

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        queue = deque()
        for i in range(len(tickets)):
            queue.append(i)
        
        time = 0
        while queue:
            time += 1
            front = queue.popleft()
            tickets[front] -= 1
            if k == front and tickets[front] == 0:
                return time
            if tickets[front] != 0:
                queue.append(front)
            
        return time