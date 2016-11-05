import stenography

import unittest

class TestBitReader(unittest.TestCase):
    def test_bit_reader(self):
        bit_reader = stenography.BitReader("rasim.txt")
        bits = []
        while True:
            bit = bit_reader.read_bit()
            if bit == -1:
                break
            bits.append(bit)
            test_bits = "010100100110000101110011"
            test_bits = list(map(int, test_bits))
        self.assertListEqual(bits[:len(test_bits)], test_bits)
        ending_byte = list(map(int, "00100001"))
        self.assertListEqual(bits[-8:], ending_byte)

if __name__ == '__main__':
    unittest.main()