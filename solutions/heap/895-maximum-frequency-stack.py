class FreqStack:

    def __init__(self):
        self.frequency_heap = []
        self.freq = defaultdict(int)
        self.calls = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        heapq.heappush(self.frequency_heap, (-self.freq[val], -self.calls, val))
        self.calls += 1


    def pop(self) -> int:
        frqeuency, index, val = heapq.heappop(self.frequency_heap)
        self.freq[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
