class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        if len(self.data) is self.capacity:
            if self.current >= self.capacity:
                self.current = 0
                self.data[self.current] = item
            else:
                self.data[self.current] = item
            self.current += 1
        else:
            self.data.append(item)

    def get(self):
        return self.data
