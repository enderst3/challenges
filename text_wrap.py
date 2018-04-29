"""
Task

You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.

Input Format

The first line contains a string, S. 
The second line contains the width, w.

Constraints

0<len(S)<10000<len(S)<1000 
0<w<len(S)0<w<len(S)

Output Format
Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""
import textwrap

def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    return '\n'.join(i for i in wrapped)