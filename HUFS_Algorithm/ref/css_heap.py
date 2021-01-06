class Heap:
    def __init__(self, L=[]):
        self.A = L

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:
            L, R = 2 * k + 1, 2 * k + 2
            if self.A[L] > self.A[k]:
                m = L
            else:
                m = k

            if R < n and self.A[R] > self.A[m]:
                m = R

            if m != k:
                self.A[m], self.A[k] = self.A[k], self.A[m]
                k = m
            else:
                break

    def make_heap(self):
        n = len(self.A)
        for k in range(n - 1, -1, -1):
            self.heapify_down(k, n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A) - 1, -1, -1):  # start 인자는 변하면 안되므로
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n -= 1
            self.heapify_down(0, n)

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    def delete_max(self):
        if len(self.A) == 0:
            return None
        key = self.A[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key


# S = [int(x) for x in input().split()]
S = [3, 8, 4, 5, 1, 15, 7, 16, 9, 2]
H = Heap(S)
H.make_heap()
print(H)
H.heap_sort()

print(H)

"""
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


"""