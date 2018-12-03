"""
The bloody photocopier is broken... Just as you were sneaking around the office to print off 
your favourite binary code!

Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string.
"""

def broken(inp):
    out = ''
    for i in inp:
        if i == '1':
            out = out + '0'
        elif i == "0":
            out = out + '1'
        else:
            pass
    return out


def broken(inp):
    """Replace each '0' with '1' and vice versa."""
    return inp.translate(str.maketrans("01", "10"))