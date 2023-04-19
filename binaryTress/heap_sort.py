import random
import time

import matplotlib.pyplot as plt


class Heap:
    def __init__(self):
        self.heap = []

    def add(self, element):
        self.heap.append(element)
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_indexes(self):
        return range(len(self.heap))

    def shift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        max_index = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[max_index]:
            max_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[max_index]:
            max_index = right_child_index
        if index != max_index:
            self.swap(index, max_index)
            self.shift_down(max_index)

    def is_leaf(self, index):
        return 2 * index + 1 >= len(self.heap)

    def is_root(self, index):
        return index == 0

    def assign_hierarchy(self, index):
        parent_index = (index - 1) // 2
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        parent = self.heap[parent_index] if parent_index >= 0 else None
        left_child = self.heap[left_child_index] if left_child_index < len(self.heap) else None
        right_child = self.heap[right_child_index] if right_child_index < len(self.heap) else None
        return parent, left_child, right_child

    def pop(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.shift_down(0)
        return root

    # def visualize(self):
    #     if not self.heap:
    #         print("Heap is empty")
    #         return
    #
    #     fig, ax = plt.subplots()
    #     ax.axis('off')
    #
    #     # Build a list of node positions
    #     positions = {}
    #     for i, node in enumerate(self.heap):
    #         level = i.bit_length() - 1
    #         pos = 2 ** level
    #         offset = i - 2 ** level
    #         x = pos / (2 ** (level + 1))
    #         y = -level
    #         positions[node] = (x + offset, y)
    #
    #     # Plot the nodes and edges
    #     for node, (x, y) in positions.items():
    #         ax.text(x, y, str(node), fontsize=12, ha='center', va='center',
    #                 bbox=dict(facecolor='white', edgecolor='gray', boxstyle='circle'))
    #         parent = positions.get(self.heap[(self.heap.index(node) - 1) // 2])
    #         if parent:
    #             ax.plot([x, parent[0]], [y, parent[1]], color='gray')
    #
    #     plt.show()


def heap_sort(arr):
    heap = Heap()
    for element in arr:
        heap.add(element)
    sorted_arr = []
    for i in heap.get_indexes():
        sorted_arr.append(heap.pop())
    return sorted_arr


def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time


def main():
    vector_lengths = [100, 500, 1000, 2000]
    times = [[] for _ in range(len(vector_lengths))]
    for i, vector_length in enumerate(vector_lengths):
        for _ in range(100):
            arr = [random.randint(0, 5000) for _ in range(vector_length)]
            time_elapsed = measure_time(heap_sort, arr)
            times[i].append(time_elapsed)
    plt.plot(vector_lengths, [sum(time_list) / len(time_list) for time_list in times])
    plt.xlabel("Vector length")
    plt.ylabel("Time elapsed (s)")
    plt.legend(["Heap sort"])
    plt.show()


if __name__ == '__main__':
    main()
