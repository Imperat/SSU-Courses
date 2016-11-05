import sys

try:
    file = sys.argv[1]
    key = sys.argv[2]
except KeyError:
    print "To few argument! Please, input input file and key"
content = ""

def magic(content, key):
    new_content = []
    for symbol in content:
        new_content.append(chr(ord(symbol) ^ key))
    return "".join(new_content)

with open(file, 'r') as f:
    content = f.read()
    content = magic(content, int(key))
    f.close()

with open(file, 'w') as f:
    f.write(content)
    f.close()