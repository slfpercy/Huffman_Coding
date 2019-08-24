import sys
import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        if other is None:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq < other.freq


def codes_dictionary(node, cod):
    codes = {}
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = cod
        return codes

    codes.update(codes_dictionary(node.left_child, cod + '0'))
    codes.update(codes_dictionary(node.right_child, cod + '1'))
    return codes


def huffman_encoding(data):
    codes = {}
    freq_char = {}
    freq_table = []
    treenode = None
    encoded = ''

    for char in data:
        if char in freq_char:
            freq_char[char] += 1
        else:
            freq_char[char] = 1

    if len(freq_char) == 1:
        for keys in freq_char:
            key = keys
        treenode = Node(None, 1)
        treenode.left_child = Node(key, 1)
        codes.update({key: "0"})
    else:
        for char in freq_char:
            node = Node(char, freq_char[char])
            heapq.heappush(freq_table, node)

        while len(freq_table) > 1:
            node1 = heapq.heappop(freq_table)
            node2 = heapq.heappop(freq_table)

            treenode = Node(None, node1.freq + node2.freq)
            treenode.left_child = node1
            treenode.right_child = node2

            heapq.heappush(freq_table, treenode)

            codes = codes_dictionary(treenode, '')

    for char in data:
        encoded += codes[char]

    return encoded, treenode


def huffman_decoding(data, tree):
    decoded = ''
    current_node = tree
    for num in data:
        if num == '0':
            if current_node.left_child.char is None:
                current_node = current_node.left_child
            else:
                decoded += current_node.left_child.char
                current_node = tree
        else:
            if current_node.right_child.char is None:
                current_node = current_node.right_child
            else:
                decoded += current_node.right_child.char
                current_node = tree

    return decoded