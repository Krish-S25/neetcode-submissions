class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.count_group = defaultdict(list)
        self.max_freq = 0 

    def push(self, val: int) -> None:
        self.freq[val] += 1
        current_val = self.freq[val]
        self.count_group[current_val].append(val)

        if current_val > self.max_freq:
            self.max_freq = current_val

    def pop(self) -> int:
        val = self.count_group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.count_group[self.max_freq]:
            self.max_freq -= 1
        
        return val

        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()