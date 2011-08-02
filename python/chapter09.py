
""" Chapter 9: Quicksort """

import sys

def basic_partition(sequence, l, r):
    """Returns the index of the partition element of a sequence, where all the elements
    left of the partition element are <= the partition element and all the elements to
    the right are >= the partition element.
    """
    partition = sequence[r]
    hold = sequence[l]; sequence[l] = -sys.maxint - 1
    i, j, temp = l, r, None
    while i <= j:
        i += 1; j -= 1
        while sequence[i] < partition: i += 1
        while sequence[j] > partition: j -= 1
        temp = sequence[i]; sequence[i] = sequence[j]; sequence[j] = temp
    sequence[j] = sequence[i]; sequence[i] = partition; sequence[r] = temp
    if partition >= hold:
        sequence[l] = hold
    else:
        i -= 1
        sequence[i+1] = hold; sequence[l] = sequence[i]; sequence[i] = partition
    return i

def median3_partition(sequence, l, r):
    """Returns the index of the partition element of a sequence, where all the elements
    left of the partition element are <= the partition element and all the elements to
    the right are >= the partition element.
    """
    swap(sequence, (r-l)/2+l, r-1)
    first, mid, last = l, r-1, r
    if sequence[first] > sequence[mid]:
        swap(sequence, first, mid); temp = mid; mid = first; first = temp;
    if sequence[mid] > sequence[last]:
        swap(sequence, mid, last); temp = last; last = mid; mid = temp;
    if sequence[first] > sequence[mid]:
        swap(sequence, first, mid)
    partition = sequence[r-1]
    i, j, temp = l, r-1, None
    while i <= j:
        i += 1; j -= 1
        while sequence[i] < partition: i += 1
        while sequence[j] > partition: j -= 1
        temp = sequence[i]; sequence[i] = sequence[j]; sequence[j] = temp
    sequence[j] = sequence[i]; sequence[i] = partition; sequence[r-1] = temp
    return i

def swap(sequence, i, j):
    """Swaps index i with index j in sequence.
    """
    temp = sequence[i]; sequence[i] = sequence[j]; sequence[j] = temp

def recursive_quicksort(sequence, l=None, r=None, partition=median3_partition):
    """Returns a sorted sequence, in ascending order.
    """
    l = 0 if l is None else l
    r = len(sequence) - 1 if r is None else r
    if r - l > 2:
        i = partition(sequence, l, r)
        recursive_quicksort(sequence, l, i-1, partition)
        recursive_quicksort(sequence, i+1, r, partition)
    else:
        insertion_sort(sequence, l, r)
    return sequence

def quicksort(sequence, partition=median3_partition):
    """Returns a sorted sequence, in ascending order.
    """
    l = 0; r = len(sequence) - 1
    num_elements = r - l
    if num_elements <= 0:
        return sequence
    elif num_elements <= 2:
        return insertion_sort(sequence, l, r)
    stack = list()
    i = partition(sequence, l, r)
    if i-l > r-i:
        stack.append(r); stack.append(i+1); r = i-1
    else:
        stack.append(i-1); stack.append(l); l = i+1
    while True:
        if r-l > 2:
            i = partition(sequence, l, r)
            if i-l > r-i:
                stack.append(r); stack.append(i+1); r = i-1
            else:
                stack.append(i-1); stack.append(l); l = i+1
        else:
            insertion_sort(sequence, l, r)
            if not stack:
                break
            l = stack.pop(); r = stack.pop()
    return sequence

def insertion_sort(sequence, l, r):
    """Returns the sequence, sorted in ascending order.
    """
    if r-l > 0:
        for i in xrange(l, r+1):
            num, j = sequence[i], i
            while j > 0 and num < sequence[j-1]:
                sequence[j] = sequence[j-1]
                j -= 1
            sequence[j] = num
    return sequence
