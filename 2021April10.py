def to_binary(n):
    binary = []
    q = n // 2
    r = n % 2
    binary = [r]
    while q != 0:
        r = q % 2
        q = q // 2
        binary.append(r)
    binary.reverse()
    return binary

def to_decimal(b):
    d = 0
    for i in b:
        d = 2 * d + i
    return d

def reverse_bit(n):
    b = to_binary(n)
    b.reverse()
    return to_decimal(b)

print(to_binary(89))
print(reverse_bit(89))
