import heapq
from collections import Counter
import matplotlib.pyplot as plt 

def read_txt(filename):
    with open(filename,'r', encoding='utf-8') as f:
        data = f.read()
    return data

def huffman_coding(frequencies):
    def build_huffman_tree(freq):
        heap = [[weight, [char, ""]] for char, weight in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return heap[0]

    def generate_huffman_codes(huffman_tree):
        codes = {}
        for pair in huffman_tree[1:]:
            char, code = pair
            codes[char] = code
        return codes

    if not frequencies:
        return {}

    freq_counter = Counter(frequencies)
    huffman_tree = build_huffman_tree(freq_counter)
    huffman_codes = generate_huffman_codes(huffman_tree)

    return huffman_codes

def show_lowercase_frequency_plot(ascii_freq):
    lowercase_characters = []
    lowercase_frequencies = []

    for i in range(26):
        char = chr(ord('a')+i)
        lowercase_characters.append(chr(ord('a')+i))
        lowercase_frequencies.append(ascii_freq.get(char,0))

    # Create a bar plot
    plt.bar(lowercase_characters, lowercase_frequencies)
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.title('Frequency of Characters in War and Peace - Leo Tolstoy')
    plt.show()

def write_bits_to_file(filename, bits):
    with open(filename, 'wb') as file:
        # Convert bits to bytes
        byte_data = bytearray()
        current_byte = 0
        bit_count = 0

        for bit in bits:
            current_byte = (current_byte << 1) | bit
            bit_count += 1

            if bit_count == 8:
                byte_data.append(current_byte)
                current_byte = 0
                bit_count = 0

        # If there are remaining bits, pad with zeros
        if bit_count > 0:
            current_byte <<= (8 - bit_count)
            byte_data.append(current_byte)

        file.write(byte_data)

text = read_txt("war-and-peace.txt")

ascii_freq = {}
mx = 0
for char in text:
    ascii_freq[char] = ascii_freq.get(char,0)+1

show_lowercase_frequency_plot(ascii_freq)
huffman_codes = huffman_coding(ascii_freq)

encoded_bits = []

for char in text:
    for b in huffman_codes[char]:
        encoded_bits.append(ord(b)-ord('0'))

write_bits_to_file("war-and-peace-compressed.txt",encoded_bits)



