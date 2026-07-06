import heapq as pq 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
                             #turning min-heap to max-heap by invertng sign
        mxheap = [-f for f in freq.values()] 
        pq.heapify(mxheap)

        Q = collections.deque()
        time = 0

        while mxheap or Q :
            time+=1
            if mxheap:
                cnt = pq.heappop(mxheap) + 1 # +1 because of -ve freq

                if cnt:
                    Q.append([cnt, time + n]) # time + n shows the nearest available next slot

            if Q and Q[0][1] == time:
                    pq.heappush(mxheap, Q.popleft()[0])

        return time