f = open("input.txt", "rb")
try:
    byte = f.read(1)
    while byte != "":
        pass
        # Do stuff with byte.
        byte = f.read(1)
        if byte:
            print ord(byte)
finally:
        f.close()
