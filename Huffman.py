import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    huffman_code = {}
    _generate_huffman_code(root, "", huffman_code)
    return huffman_code

def _generate_huffman_code(node, current_code, huffman_code):
    if node is None:
        return
    if node.char is not None:
        huffman_code[node.char] = current_code
    _generate_huffman_code(node.left, current_code + "0", huffman_code)
    _generate_huffman_code(node.right, current_code + "1", huffman_code)

# Example usage
frequency = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
codes = huffman_codes(frequency)
print("Huffman Codes:", codes)
