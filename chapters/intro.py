
def gcd(u, v):
    """Returns the greatest common denominator (or greatest common factor) of
    u and v.
    """
    if v == 0:
        return u
    return gcd(v, u%v)

def lowest_terms(numerator, denominator):
    """Given a numerator and denominator (representing a fraction), returns a tuple
    of the fraction in its lowest terms.
    """
    d = gcd(numerator, denominator)
    return (numerator/d, denominator/d)
