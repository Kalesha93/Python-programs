import heapq
numbers = [20, 5, 15, 10, 30, 25]

heapq.heapify(numbers)
print("Min-Heap:", numbers)
heapq.heappush(numbers, 8)
print("After pushing 8:", numbers)
smallest = heapq.heappop(numbers)
print("Popped smallest:", smallest)
print("Heap now:", numbers)
print("Smallest element:", numbers[0])
