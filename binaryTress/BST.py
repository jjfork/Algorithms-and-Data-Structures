import random
import time

import matplotlib.pyplot as plt


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, current_node):
        if val < current_node.val:
            if current_node.left_child == None:
                current_node.left_child = Node(val)
            else:
                self._insert(val, current_node.left_child)
        elif val > current_node.val:
            if current_node.right_child == None:
                current_node.right_child = Node(val)
            else:
                self._insert(val, current_node.right_child)
        else:
            print("Value already in tree")

    def search(self, val):
        if self.root != None:
            return self._search(val, self.root)
        else:
            return False

    def _search(self, val, current_node):
        if val == current_node.val:
            return True
        elif val < current_node.val and current_node.left_child != None:
            return self._search(val, current_node.left_child)
        elif val > current_node.val and current_node.right_child != None:
            return self._search(val, current_node.right_child)
        return False


def create_random_vector(length):
    vec = list(range(1, length + 1))
    random.shuffle(vec)
    return vec


def measure_search_time(bst, vec):
    start_time = time.time()
    for val in vec:
        bst.search(val)
    end_time = time.time()
    return end_time - start_time


vector_lengths = [100, 500, 1000, 2000]
num_trials = 100
avg_times = [[] for _ in range(len(vector_lengths))]

for i, length in enumerate(vector_lengths):
    for j in range(num_trials):
        vec = create_random_vector(length)
        bst = BST()
        for val in vec:
            bst.insert(val)
        search_vec = random.sample(vec, 10)
        avg_times[i].append(measure_search_time(bst, search_vec))

plt.plot(vector_lengths, [sum(times) / num_trials for times in avg_times])
plt.xlabel('Length of Vector')
plt.ylabel('Average Search Time (s)')
plt.title('Average Search Time in Binary Search Tree')
plt.show()
