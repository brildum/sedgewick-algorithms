
""" Chapter 19: String Searching """

def brute_force_search(pattern, string):
    """Returns the index of the first match, or -1 if there is no match.
    """
    plen, slen = len(pattern), len(string)
    i, j = 0, 0
    while i < slen and j < plen:
        if string[i] == pattern[j]:
            j += 1
        else:
            i -= j
            j = 0
        i += 1
    if j == plen:
        return i - plen
    else:
        return -1

def knuth_morris_pratt_search(pattern, string):
    """Returns the index of the first match, or -1 if there is no match.
    """
    plen, slen = len(pattern), len(string)
    # Preprocess pattern and generate next table
    next = [-1]
    i, j = 0, -1
    while i < plen:
        if j == -1 or pattern[i] == pattern[j]:
            j += 1; i += 1; next.append(j)
        else:
            j = next[j]

    # Search through the string
    i, j = 0, 0
    while i < slen:
        if string[i] == pattern[j]:
            j += 1; i += 1
            if j == plen:
                return i - plen
        else:
            j = next[j]
            if j == 0:
                i += 1
    return -1

# TODO Implement Boyer-Moore string searching algorithm

def robin_karp_search(pattern, string):
    """Returns the index of the first match, or -1 if there is no match.
    """
    m, n = len(pattern), len(string)
    alphabet_size, big_prime = 256, 33554393
    # dm is the value to subtract the left-most digit from in the calculation
    # to get the next hashed value
    dm = 1
    for i in xrange(m-1):
        dm = (alphabet_size * dm) % big_prime
    pattern_hash = 0
    for i in xrange(m):
        pattern_hash = (pattern_hash * alphabet_size + ord(pattern[i])) % big_prime
    hash = 0
    for i in xrange(m):
        hash = (hash * alphabet_size + ord(string[i])) % big_prime
    i, stop = 0, n - m
    while pattern_hash != hash and i < stop:
        hash = (hash + alphabet_size * big_prime - ord(string[i]) * dm) % big_prime
        hash = (hash * alphabet_size + ord(string[i+m])) % big_prime
        i += 1
    if pattern_hash == hash:
        return i
    else:
        return -1
