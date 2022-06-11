from re import M


def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0

    while i < len(s):
        m = int(s[i])
        if m % 2 == 1:
            k += m
        i += 1
    return k