def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    j = 0
    i = 0
    while i < len(s): 
        if int(s[i])%2 == 0:
            j+=1
        i+=1
    return j
print(main('1234'))