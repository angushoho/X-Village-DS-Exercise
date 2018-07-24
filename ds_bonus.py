from lib.stack import Stack

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    tmp = Stack()
    string = ""
    while dec_number != 0:
        tmp.push(dec_number % base)
        dec_number //= base
    while not tmp.isEmpty():
        string += digits[tmp.pop()]
    
    return string

print(base_converter(1000, 10))
print(base_converter(500, 12))