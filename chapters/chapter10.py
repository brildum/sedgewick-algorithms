
""" Chapter 10: Radix Sorting """

def radix_exchange_sort(sequence, bit_offset=None, l=None, r=None):
    """Returns a sequence of integers in sorted (ascending) order. Assumes the
    sequence has integers which can be represented by no more than bit_offset + 1 bits.
    (default is 32 bits)
    """
    bit_offset = bit_offset if bit_offset is not None else 31
    l = l if l is not None else 0
    r = r if r is not None else len(sequence) - 1
    if r > l and bit_offset >= 0:
        i, j = l, r
        while i < j:
            while i < j and bits(sequence[i], bit_offset, 1) == '0': i += 1
            while i < j and bits(sequence[j], bit_offset, 1) == '1': j -= 1
            swap(sequence, i, j)
        if bits(sequence[r], bit_offset, 1) == '0': j += 1
        radix_exchange_sort(sequence, bit_offset-1, l, j-1)
        radix_exchange_sort(sequence, bit_offset-1, j, r)
    return sequence

def radix_sort(sequence, max_num, b=8):
    """Returns a sequence of integers in sorted (ascending) order. Assumes the
    sequence has integers which are between 0 and max_num.
    """
    temp = list(sequence)
    for p in xrange(max_num / (2 ** b) + 1):
        count = [0] * (2 ** b)
        for num in temp:
            count[int(bits(num, p*b, b), 2)] += 1
        for j in xrange(1, len(count)):
            count[j] += count[j-1]
        for i in xrange(len(sequence)-1, -1, -1):
            index = int(bits(sequence[i], p*b, b), 2)
            temp[count[index]-1] = sequence[i]
            count[index] -= 1
        for i in xrange(len(temp)):
            sequence[i] = temp[i]
    return sequence

def bits(num, offset, num_bits):
    """Returns a string bit representation of length num_bits which matches num's
    bit representation between offset and offset - num_bits bits.
    """
    # TODO: Use Python bit manipulation features
    # binary numbers have 0b at the beginning of the string
    binary = bin(num)[2:]
    required_length = offset + num_bits
    diff = required_length - len(binary)
    if diff > 0:
        binary = ('0' * diff) + binary
    start = len(binary) - required_length
    return binary[start:start+num_bits]

def swap(sequence, i, j):
    temp = sequence[i]; sequence[i] = sequence[j]; sequence[j] = temp
