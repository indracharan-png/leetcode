import heapq


class MedianFinder:

    def __init__(self):
        self.low_to_mid_heap = []
        self.mid_to_high_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low_to_mid_heap, -num)
        heapq.heappush(self.mid_to_high_heap, -heapq.heappop(self.low_to_mid_heap))
        if len(self.mid_to_high_heap) > len(self.low_to_mid_heap):
            heapq.heappush(self.low_to_mid_heap, -heapq.heappop(self.mid_to_high_heap))
        return
          
        

    def findMedian(self) -> float:
        if (len(self.low_to_mid_heap) + len(self.mid_to_high_heap)) % 2 == 0:
            return (-(self.low_to_mid_heap[0]) + self.mid_to_high_heap[0]) / 2
        return -self.low_to_mid_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()