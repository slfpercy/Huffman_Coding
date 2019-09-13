import sys
from coding import huffman_encoding, huffman_decoding

if __name__ == "__main__":
    print("Test: \n")
    sentence = "I am a test sentence, you could change me to see how the code works"

    print("The size of the sentence is: {}\n".format(sys.getsizeof(sentence)))
    print("The content of the sentence is: {}\n".format(sentence))

    encoded_data, tree = huffman_encoding(sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print("The original and decoded data are the same?:", sentence == decoded_data)
