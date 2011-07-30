
def swap(sequence, i, j):
    """Swaps elements at specified indices in a sequence.
    """
    temp = sequence[i]
    sequence[i] = sequence[j]
    sequence[j] = temp

def selection_sort(sequence):
    """Returns the sequence, sorted in ascending order.
    """
    seq_len = len(sequence)
    if seq_len > 1:
        for i in xrange(seq_len-1):
            min_index = i
            for j in xrange(i+1, seq_len):
                if sequence[min_index] > sequence[j]:
                    min_index = j
            swap(sequence, i, min_index)
    return sequence

def insertion_sort(sequence):
    """Returns the sequence, sorted in ascending order.
    """
    seq_len = len(sequence)
    if seq_len > 1:
        for i in xrange(1, seq_len):
            num, j = sequence[i], i
            while j > 0 and num < sequence[j-1]:
                sequence[j] = sequence[j-1]
                j -= 1
            sequence[j] = num
    return sequence

H_VALUES = (11, 7, 3, 1)
def shell_sort(sequence, h_values=H_VALUES):
    """Returns the sequence, sorted in ascending order.
    """
    seq_len = len(sequence)
    if seq_len > 1:
        for h in h_values:
            for i in xrange(h, seq_len, h):
                num, j = sequence[i], i
                while j-h >= 0 and num < sequence[j-h]:
                    sequence[j] = sequence[j-h]
                    j -= h
                sequence[j] = num
    return sequence

def bubble_sort(sequence):
    """Returns the sequence, sorted in ascending order.
    """
    seq_len = len(sequence)
    if seq_len > 1:
        swapped_values = True
        while swapped_values:
            swapped_values = False
            for i in xrange(1, seq_len):
                if sequence[i] < sequence[i-1]:
                    swap(sequence, i, i-1)
                    swapped_values = True
    return sequence

def distribution_count_sort(sequence, max_num):
    """Returns the sequence, sorted in ascending order provided that the
    sequence contains elements in the range of 0 and max_num.
    """
    seq_len = len(sequence)
    if seq_len > 1:
        counts = [0] * (max_num + 1)
        for num in sequence:
            counts[num] += 1
        i = seq_len - 1
        for j in xrange(max_num, -1, -1):
            count = counts[j]
            while count:
                sequence[i] = j; count -=1; i -= 1;
    return sequence
