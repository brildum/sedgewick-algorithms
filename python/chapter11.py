
""" Chapter 11: Priority Queues """

import copy

class MaxHeap(object):
    """Collection of objects where pop always returns the greatest object.
    """
    def __init__(self, heap=None):
        self.heap = list() if heap is None else copy.deepcopy(heap)
        if self.heap:
            self._heapify()

    def insert(self, item):
        """Adds a new item to the heap.
        """
        self.heap.append(item)
        self._upheap(len(self.heap) - 1)

    def replace(self, item):
        """Replaces the top-element of the heap with a new item (unless the new item is larger).
        """
        if len(self.heap) > 0 and item < self.heap[0]:
            self.heap[0] = item
            self._downheap(0)

    def remove(self):
        """Removes the top-element from the heap.
        """
        length = len(self.heap)
        if length > 1:
            self.heap[0] = self.heap.pop()
            self._downheap(0)
        elif length == 1:
            self.heap.pop()

    def get(self):
        """Returns the top-element from the heap.
        """
        if self.heap:
            return self.heap[0]
        else:
            return None

    def _heapify(self):
        """Ensures the entire heap maintains the heap property.
        """
        mid_index = (len(self.heap) / 2) - 1
        for i in xrange(mid_index, -1, -1):
            self._downheap(i)

    def _upheap(self, index):
        """Ensures the heap maintains the heap property from bottom to top.
        """
        value = self.heap[index]
        parent = self._parent(index)
        while parent >= 0 and self.heap[parent] < value:
            self.heap[parent] = self.heap[index]
            index = parent; parent = self._parent(index)
        self.heap[index] = value

    def _downheap(self, index):
        """Ensures the heap maintains the heap property from top to bottom.
        """
        # TODO: May want to clean this up so the logic is a bit clearer
        value = self.heap[index]
        n = len(self.heap)
        while True:
            li, ri = self._children(index)
            if li < n:
                if ri < n:
                    if self.heap[li] > self.heap[ri]:
                        if self.heap[li] > value:
                            self.heap[index] = self.heap[li]
                            index = li
                        else:
                            break
                    else:
                        if self.heap[ri] > value:
                            self.heap[index] = self.heap[ri]
                            index = ri
                        else:
                            break
                else:
                    if self.heap[li] > value:
                        self.heap[index] = self.heap[li]
                        index = li
                    else:
                        break
            elif ri < n:
                if self.heap[ri] > value:
                    self.heap[index] = self.heap[ri]
                    index = ri
                else:
                    break
            else:
                break
        self.heap[index] = value

    def _parent(self, index):
        """Returns the parent index of index.
        """
        return (index - 1) / 2

    def _children(self, index):
        """Returns the two (left, right) child indices of index.
        """
        left = (2 * index) + 1
        return left, left + 1

def heap_sort(sequence):
    heap = MaxHeap(sequence)
    for i in xrange(len(sequence)-1, -1, -1):
        sequence[i] = heap.get()
        heap.remove()
    return sequence
