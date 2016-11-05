import os
from os import path


class Encryptor(object):
    def __init__(self):
        self.key = 21

    def encrypt(self, patch):
        for p, _, files in os.walk(patch):
            for file in files:
                self.encrypt_file(file, p)
        self.encrypt_folders(patch)

    def encrypt_folders(self,patch):
       for p, f, _ in os.walk(patch):
           for folder in f:
               os.rename(path.join(p, folder),
                         path.join(p, self.encrypt_string(folder)))

    def decrypt(self, patch):
        self.encrypt(patch)

    def encrypt_file(self, filename, p):
        with open(path.join(p, filename), 'rb') as f:
            with open(path.join(p, self.encrypt_string(filename)),
                      'wb') as r:

                current_byte = f.read(1)
                while current_byte:
                    current_byte = self.magic(current_byte)
                    r.write(current_byte)
                    current_byte = f.read(1)
        os.remove(path.join(p, filename))

    def decrypt_file(self, filename, p):
        return self.encrypt_file(filename, p)

    def encrypt_string(self, s):
        s = list(s)
        r = list()
        for i in s:
            j = self.magic(i)
            r.append(j)
        return ''.join(r)

    def magic(self, byte):
        return chr(ord(byte) ^ self.key)

if __name__ == '__main__':
    e = Encryptor()
    e.encrypt("test_user")

