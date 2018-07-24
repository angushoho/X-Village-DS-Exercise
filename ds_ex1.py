from lib.stack import Stack

def dec_to_bin(dec):
    tmp = Stack()
    binary = ""
    while dec != 0:
        tmp.push(dec % 2)
        dec //= 2
    while not tmp.isEmpty():
        binary += str(tmp.pop())
    return binary

print(dec_to_bin(42))
print(dec_to_bin(100))