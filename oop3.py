class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

c = Counter()
c.increment()
c.increment()
c.increment()
print("Counter Value:", c.value)