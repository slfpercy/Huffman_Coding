import sys
import heapq


class Node:
    """
    This is the Node class which will contain the character properties in the huffman tree.
    """
    def __init__(self, char, freq):
        """
        Every node will contain a character, the frequency of the character and if necessary child nodes for other
        characters
        :param char: character
        :param freq: frequency of the char
        """
        self.char = char
        self.freq = freq
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        """
        It will be necessary to compare the nodes with others. This function allows to compare the node class with other
        node classes (It's frequencies)
        :param other:
        :return:
        """
        if other is None:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq < other.freq


def codes_dictionary(node, cod):
    """
    Create a dictionary with the binary codes for every character in the huffman tree using recursion
    :param node:
    :param cod:
    :return:
    """
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
    tree_node = None
    encoded = ''

    for char in data:
        if char in freq_char:
            freq_char[char] += 1
        else:
            freq_char[char] = 1

    if len(freq_char) == 1:
        for keys in freq_char:
            key = keys
        tree_node = Node(None, 1)
        tree_node.left_child = Node(key, 1)
        codes.update({key: "0"})
    else:
        for char in freq_char:
            node = Node(char, freq_char[char])
            heapq.heappush(freq_table, node)

        while len(freq_table) > 1:
            node1 = heapq.heappop(freq_table)
            node2 = heapq.heappop(freq_table)

            tree_node = Node(None, node1.freq + node2.freq)
            tree_node.left_child = node1
            tree_node.right_child = node2

            heapq.heappush(freq_table, tree_node)

            codes = codes_dictionary(tree_node, '')

    for char in data:
        encoded += codes[char]

    return encoded, tree_node


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
