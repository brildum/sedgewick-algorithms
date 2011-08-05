
""" Chapter 12: Selection and Merging """

import random
import sys

MIN_INT = -sys.maxint - 1

def select(sequence, k, l=None, r=None):
    """Returns the kth smallest element of sequence.
    """
    k -= 1
    l = 0 if l is None else l
    r = len(sequence)-1 if r is None else r
    while l < r:
        i = partition(sequence, l, r)
        if i > k:
            r = i-1
        elif i < k:
            l = i+1
        else:
            return sequence[k]
    return sequence[l]

def partition(sequence, l, r):
    """Returns the index of an element in the sequence such that smaller elements
    are to the left and greater elements are to the right.
    """
    if r - l > 1:
        partition = random.randint(l, r)
        swap(sequence, partition, r)
        hold = sequence[l]; sequence[l] = MIN_INT
        i, j, temp = l-1, r, None
        while i < j:
            i += 1; j -= 1
            while sequence[i] < sequence[r]: i += 1
            while sequence[j] > sequence[r]: j -= 1
            temp = sequence[i]; sequence[i] = sequence[j]; sequence[j] = temp
        sequence[j] = sequence[i]; sequence[i] = sequence[r]; sequence[r] = temp
        if hold <= sequence[i]:
            sequence[l] = hold
        else:
            swap(sequence, l, i-1); sequence[i-1] = sequence[i]; sequence[i] = hold
            i -= 1
        return i
    else:
        if sequence[r] < sequence[l]:
            swap(sequence, r, l)
        return l

def swap(sequence, i, j):
    temp = sequence[i]; sequence[i] = sequence[j]; sequence[j] = temp

def merge_sort(sequence):
    """Returns the sequence, sorted in ascending order.
    """
    l, r = 0, len(sequence) - 1
    if l < r:
        mid = ((r + l) / 2) + 1
        left, right = sequence[l:mid], sequence[mid:r+1]
        sequence = merge(sequence, merge_sort(left), merge_sort(right))
    return sequence

def merge(sequence, left, right):
    """Merges two sorted sequences into sequence.
    """
    llen, rlen = len(left), len(right)
    a, b = 0, 0
    for i in xrange(llen + rlen):
        if a < llen:
            if b < rlen:
                if left[a] <= right[b]:
                    sequence[i] = left[a]; a += 1
                else:
                    sequence[i] = right[b]; b += 1
            else:
                sequence[i] = left[a]; a += 1
        else:
            sequence[i] = right[b]; b += 1
    return sequence
