import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
    def push(self, val):
        heapq.heappush(self.heap, -val) 
    def pop(self):
        return -heapq.heappop(self.heap) if self.heap else None

    def peek(self):
        return -self.heap[0] if self.heap else None

heap = MaxHeap()
nums = [10, 20, 5, 30, 15]

for n in nums:
    heap.push(n)

print("Max element:", heap.peek())  

print("Pop elements in order:")
while heap.peek() is not None:
    print(heap.pop(), end=" ") 
