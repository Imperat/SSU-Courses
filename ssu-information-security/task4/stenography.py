import argparse

class BitReader(object):
    def __init__(self, filename):
        self.filename = filename
        self.content = None
        self.pos = 0
        self.pos_in_byte = 0

    def read_bit(self):
        if self.content is None:
            file = open(self.filename, 'rb')
            content = file.read()
            file.close()
        if self.pos > len(content) - 1:
            return -1
        bit = BitReader.get_bit(content[self.pos], self.pos_in_byte)
        self.pos_in_byte += 1
        if self.pos_in_byte == 8:
            self.pos_in_byte = 0
            self.pos += 1
        return bit

    @staticmethod
    def get_bit(byte, pos_in_byte):
        helpers = [128, 64, 32, 16, 8, 4, 2, 1]
        if ord(byte) & helpers[pos_in_byte] == 0:
            return 0
        return 1


class StenographyWriter(object):

    def __init__(self, filename, bit_reader=None):
        self.filename = filename
        self.bit_reader = bit_reader

    def write_message(self):
        if self.bit_reader is None:
            return
        bit = self.bit_reader.read_bit()
        with open(self.filename, 'r') as f:
            content = f.read()
            content = ' '.join(list(filter(lambda x: True if x else False, content.split(' '))))
        spaces = []
        for i, c in enumerate(content):
            if c == ' ':
                if bit == 1:
                    spaces.append(i)
                bit = self.bit_reader.read_bit()
            if bit == -1:
                break
        lim = len(spaces)
        content = list(content)
        for i in range(lim):
            content.insert(spaces[i], ' ')
            add_one = lambda x : x + 1
            add_all = lambda x : list(map(add_one, x))
            spaces = add_all(spaces)

        with open(self.filename, 'w') as f:
            for i in content:
                f.write(i)
            f.close()


    def read_message(self):
        with open(self.filename, 'r') as f:
            content = f.read()
        bits = []
        leng = len(content)
        indx = 0
        while indx < leng:
            if content[indx] == ' ':
                if content[indx+1] == ' ':
                    bits.append(1)
                    indx += 2
                    continue
                bits.append(0)
            indx += 1
        res = "".join(map(str, bits))

        lbytes = []
        beginning, offset = 0, 8
        while beginning + offset < len(res):
            current_byte = res[beginning:beginning+offset]
            lbytes.append(current_byte)
            beginning += 8

        symbols = []
        for i in lbytes:
            if int(i, 2) == 0:
                #break
                pass
            symbols.append(chr(int(i, 2)))
        return "".join(symbols)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("command",
                        help="[write], [read] or [tea]")
    parser.add_argument("-d", "--destination",
                        help="Destination file for save message")
    parser.add_argument("-m", "--message",
                        help="File with secret message")

    args = parser.parse_args()

    command = args.command

    if command == 'tea':
        print "I'm bad teapot :("
    if command == 'write':

        bit_reader = BitReader(args.message)
        stenography = StenographyWriter(args.destination,
                                        bit_reader=bit_reader)
        stenography.write_message()

    if command == 'read':
        bit_reader = BitReader(args.message)
        stenography = StenographyWriter(args.destination,
                                        bit_reader=bit_reader)
        res = stenography.read_message()
        print res
