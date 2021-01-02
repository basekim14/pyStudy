class MaxHeap:
    def __init__(self, L):
        self.queue = L[:]
        self.build_heap()

    def __str__(self):
        return str(self.queue)

    def build_heap(self):
        n = len(self.queue)
        for i in range(n//2, -1, -1):
            self.max_heapify(i, n)

    def max_heapify(self, i, n):
        left = self.left_child(i)
        right = self.right_child(i)
        biggest = i

        if right <= n-1:
            if self.queue[left] > self.queue[right]:
                biggest = left
            else:
                biggest = right
        elif left <= n-1:
            biggest = left
        else:
            return

        if self.queue[biggest] > self.queue[i]:
            self.swap(i, biggest)
            self.max_heapify(biggest, n)

    def heap_sort(self):
        n = len(self.queue)

        sorted_list = []
        for i in range(len(self.queue)-1, -1, -1):
            sorted_list.append(self.queue[0])
            self. swap(0, i)
            n -= 1
            self. max_heapify(0, n)
        return sorted_list

    def insert(self, key):      # 매개변수 자유, heaq queue push에선 매개변수 두개(리스트, key)
        self.queue.append(key)
        self.build_heap()

    @staticmethod
    def left_child(i):
        return i*2 + 1

    @staticmethod
    def right_child(i):
        return i*2 + 2

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]


num_list = [7, 9, 4, 8, 6, 3]

H = MaxHeap(num_list)
print(H)

print(H.heap_sort())