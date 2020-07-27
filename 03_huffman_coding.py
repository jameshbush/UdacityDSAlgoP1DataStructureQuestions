import sys
import queue

class Node:
    def __init__(self, freq, char=None, left=None, right=None, bit=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = None
    def __lt__(self, other): self.freq < other.freq
    def __eq__(self, other): self.freq == other.freq

def huffman_encoding(data):
    # 1) create char/freq nodes
    freqs = {}
    for char in data:
        freqs[char] = freqs.get(char, 0) + 1
    print('Encoding', freqs)

    # 2) sort nodes by frequency, use a tree and (list or mini heap)
    q = queue.PriorityQueue()
    for char, freq in freqs.items():
        freqs[char] = Node(freq, char) # replace freq int with freq node
        q.put( (freq, freqs[char]) ) # put freq node in queue

    while q.qsize() > 1:
        # 3) pop two lowest freq nodes
        left_entry = q.get()[1]
        right_entry = q.get()[1]

        # 4) combine nodes as children to freq node
        freq = left_entry.freq + right_entry.freq
        internal_node = Node(freq=freq, left=left_entry, right=right_entry)
        q.put( (freq, internal_node) )

    # 5) repeate 3&4 until there's one node
    root = q.get()[1]

    # 6) assign bit 0 to left & 1 to right children
    # traverse tree depth first
    # 7) generate unique bin code for each char
    def traverse(node, code):
        if node.left: traverse(node.left, code + '0')
        if node.right: traverse(node.right, code + '1')
        if node.char: node.code = code

    traverse(root, '')

    # for k, freq in freqs.items(): print(k, freq.code)

    # 8) encode string as bytes?
    encoded_data = ''
    for char in data: encoded_data += freqs[char].code
    return encoded_data, root

def huffman_decoding(data, tree):
    codes = {}
    def traverse(node):
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
        if node.char:
            codes[node.code] = node.char

    traverse(tree)
    print('Decoding:', codes)

    # get the max key (code) to compare first
    keys = list(codes.keys())
    max_len = len(keys[0])
    min_len = len(keys[0])
    for code in keys:
        if len(code) > max_len:
            max_len = len(code)

        if len(code) < min_len:
            min_len = len(code)

    # lookup from max length to min values in the codes
    solution = ''
    start_index = 0
    end_index = 0
    print(len(data))
    while True: # (end_index - start_index) >= min_len and end_index <=  len(code):
        start_index = end_index
        end_index = start_index + max_len

        while True:
            possible_char_code = data[start_index:end_index]
            print(start_index, '-', end_index, ':', possible_char_code)
            if start_index > len(data): # len(possible_char_code) < min_len:
                return solution
                raise('Too Small Sir')

            char = codes.get( possible_char_code )

            if char is None:
                end_index -= 1
            else:
                solution += char
                break

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print('assert("{}" == "{}") => {}'.format(decoded_data, a_great_sentence, decoded_data == a_great_sentence))
    assert(decoded_data == a_great_sentence)

    a_great_sentence = 'AAAAAAABBBCCCCCCCDDEEEEEE'

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)

    decoded_data = huffman_decoding(encoded_data, tree)
    print('assert("{}" == "{}") => {}'.format(decoded_data, a_great_sentence, decoded_data == a_great_sentence))
    assert(decoded_data == a_great_sentence)
