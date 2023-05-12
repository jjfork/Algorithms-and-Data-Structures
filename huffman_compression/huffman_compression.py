import heapq
import os
import time

import matplotlib.pyplot as plt
from natsort import natsorted
from tabulate import tabulate


class Node:
    def __init__(self, sym=None, count=None, l=None, r=None):
        self.sym = sym
        self.count = count
        self.left = l
        self.right = r

    def __lt__(self, other):
        return self.count < other.count


class HuffmanCompression:
    def __init__(self):
        self._tree = None
        self._codes = {}
        self.freq = {}

    def compress(self, text: str) -> list:
        self._count_freq(text)
        self._tree = self._build_tree()
        self._generate_code(self._tree, '')
        start = time.perf_counter_ns()
        binary_string = self.binary_string_generator(text)
        end = time.perf_counter_ns()
        compression_times.append(end - start)

        return binary_string

    def decompress(self, binary_data: list) -> str:
        text = ''
        curr_node = self._tree
        for symbol_bits in binary_data:
            for bit in symbol_bits:
                if bit == 0:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
                if self._is_leaf(curr_node):
                    text += curr_node.sym
                    curr_node = self._tree
        return text

    def binary_string_generator(self, text: str) -> list:
        binary_string = []

        for symbol in text:
            code = self._codes.get(symbol, '')
            binary_string.append(tuple(int(bit) for bit in code))
        return binary_string

    def _generate_code(self, node: Node, code: str):
        if self._is_leaf(node):
            self._codes[node.sym] = code
        else:
            self._generate_code(node.left, code + '0')
            self._generate_code(node.right, code + '1')

    def _count_freq(self, text: str) -> None:
        for symbol in text:
            if symbol not in self.freq:
                self.freq[symbol] = 0
            self.freq[symbol] += 1

    def _build_tree(self) -> Node:
        priority_queue = []
        for symbol, count in self.freq.items():
            node = Node(symbol, count)
            heapq.heappush(priority_queue, node)

        while len(priority_queue) > 1:
            left_node = heapq.heappop(priority_queue)
            right_node = heapq.heappop(priority_queue)
            new_node = Node(l=left_node, r=right_node, count=left_node.count + right_node.count)
            heapq.heappush(priority_queue, new_node)

        return priority_queue[0]

    @staticmethod
    def _is_leaf(node: Node) -> bool:
        return node.left is None and node.right is None


if __name__ == '__main__':
    # initialize the compression object
    huffman = HuffmanCompression()

    # plot the compression rate as a function of text length
    text_lengths = [348, 924, 3_622, 8_485, 16_021]
    bit_counts_before = []
    bit_counts_after = []
    compression_ratios = []
    compression_times = []
    decompression_ration = []
    decompression_times = []

    for task_file_name in natsorted(os.listdir("data")):
        with open(os.path.join("data", task_file_name), 'r') as file:
            print(file.name)
            text_to_compress = file.read()
            start_comp = time.perf_counter_ns()
            result = huffman.compress(text_to_compress)
            end_comp = time.perf_counter_ns()
            comp_time = end_comp - start_comp
            # compression_times.append(comp_time)
            # generate list of tuple with (symbol, symbol_frequency, code)
            task_structure = []

            for symbol_index in range(len(text_to_compress)):
                text_symbol = text_to_compress[symbol_index]
                element = (text_symbol, huffman.freq[text_symbol], result[symbol_index])
                task_structure.append(element)

            table = set([(symbol, count, ''.join(str(bit) for bit in code)) for symbol, count, code in task_structure])
            print(tabulate(table, headers=["Symbol", "Count", "Huffman Code"]))

            # display the compressed binary code
            binary_code = ""
            for symbol_code in result:
                binary_code += "".join([str(symbol_bit) for symbol_bit in symbol_code])

            print(f"Coded text: {binary_code}")
            start_dec = time.perf_counter_ns()
            decoded_text = huffman.decompress(result)
            end_dec = time.perf_counter_ns()
            decomp_time = end_dec - start_dec
            decompression_times.append(decomp_time)
            print("Decoded text:", decoded_text)

            original_size = len(text_to_compress) * 8
            compressed_size = len(binary_code)
            print("Original size:", original_size)
            print("Compressed size:", compressed_size)
            print(f"compression time:  {comp_time} s")
            print(f"decompression time:  {decomp_time} s")

            compression_ratio = (1 - (compressed_size / original_size)) * 100
            print("Compression ratio (in %):", compression_ratio)

            compression_ratio = (1 - (compressed_size / original_size)) * 100

            bit_counts_before.append(original_size)
            bit_counts_after.append(compressed_size)
            compression_ratios.append(compression_ratio)

    # plot the bit count before and after compression
    plt.plot(text_lengths, bit_counts_before, label="Before compression")
    plt.plot(text_lengths, bit_counts_after, label="After compression")
    plt.xlabel("Text length")
    plt.ylabel("Bits")
    plt.title("Bits before and after compression")
    plt.legend()
    plt.show()

    # plot the compression ratio as a function of text length
    plt.plot(text_lengths, compression_ratios)
    plt.xlabel("Text length")
    plt.ylabel("Compression ratio %")
    plt.title("")
    plt.show()

    # plot compression and decompression times
    plt.plot(text_lengths, compression_times, label="Compression time")
    plt.plot(text_lengths, decompression_times, label="Decompression time")
    plt.xlabel("Text length")
    plt.ylabel("Time (in s)")
    plt.title("Time compression and decompression")
    plt.legend()
    plt.show()
