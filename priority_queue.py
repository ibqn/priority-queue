class MaxPQ:
    def __init__(self):
        self.pq = [None]

    def __str__(self):
        return f"{self.pq[1:]}"

    def is_empty(self):
        return self.size() <= 1

    def size(self):
        return max(0, len(self.pq) - 1)

    def max(self):
        return self.pq[1]

    def insert(self, el):
        self.pq.append(el)

        self._swim()

    def _swim(self, n=None):
        if n == None:
            n = self.size()

        while n > 1 and self._less(n // 2, n):
            self._exchange(n, n // 2)
            n //= 2

    def _sink(self, k):
        n = self.size()
        while 2 * k <= n:
            j = 2 * k

            if j < n and self._less(j, j + 1):
                j += 1

            if not self._less(k, j):
                break

            self._exchange(k, j)
            k = j

    def _less(self, i, j):
        return self.pq[i] < self.pq[j]

    def _exchange(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def delete_max(self):
        max = self.pq[1]
        self._exchange(1, -1)
        del self.pq[-1]
        self._sink(1)

        return max


if __name__ == "__main__":
    pq = MaxPQ()

    pq.insert("B")
    pq.insert("L")
    pq.insert("E")
    pq.insert("K")

    print(pq)

    for _ in range(pq.size()):
        print("delete max", pq.delete_max())

    pq = MaxPQ()
    data = input().split()
    for key in data:
        if key == "-":
            print("delete max", pq.delete_max())
        else:
            print("insert", key)
            pq.insert(key)

    print(f"({pq.size()} items left on priority queue)")
    print(f"queue: {pq}")
