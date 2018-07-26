class MinHeap:
    def __init__(self):
        self.tree = []
        self.delete = []
    # build a new heap from a list of keys
    def build_heap(self, keys):
        self.tree = keys
        self.size = len(self.tree)
        # print(self.size)
        self.tree.insert(0, None)
        # self.size = len(self.tree)
        for i in range((len(self.tree) - 1) // 2, 0, -1):
            self.shift(i)

    def shift(self, index):
        left = index * 2
        right = index * 2 + 1
        while left <= len(self.tree) - 1:
            if self.tree[left] < self.tree[index]:
                m = self.tree[left]
                if (right) <= len(self.tree) - 1:
                    if self.tree[right] < m:
                        self.tree[right], self.tree[index] = self.tree[index], self.tree[right]
                    else:
                        self.tree[left], self.tree[index] = self.tree[index], self.tree[left]
                else:
                    self.tree[left], self.tree[index] = self.tree[index], self.tree[left]
            else:
                if (right) <= len(self.tree) - 1:
                    if self.tree[right] < self.tree[index]:
                        self.tree[right], self.tree[index] = self.tree[index], self.tree[right]
            index *= 2
            left = index * 2
            right = index * 2 + 1

    # add a new item to the heap
    def insert(self, item):
        self.tree.append(item)
        for i in range(len(self.tree) - 1 // 2, 0, -1):
            self.shift(i)

    # return the item with the minimum key value, removing the item from the heap
    def del_min(self):
        self.delete.append(self.tree[1])
        del self.tree[1]
        self.tree.insert(1, self.tree.pop())
        for i in range((len(self.tree) - 1) // 2, 0, -1):
            self.shift(i)
    # print the minimum heap on the screen
    def display(self):
        print(self.tree[1:])

heap = MinHeap()

heap.build_heap([9, 5, 6, 2, 3])
heap.display()
'''
for i in heap.tree[1:]:
    heap.del_min()
    heap.display()

print("delete list : ", heap.delete)
'''
heap.insert(1)
heap.display()
heap.insert(7)
heap.display()
heap.insert(0)
heap.display()

'''
heap.insert(1)
heap.insert(7)
heap.display()

print(heap.del_min())
print(heap.del_min())
heap.display()
'''