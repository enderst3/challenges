"""
Write a method, that replaces every nth char oldValue with char newValue.

Method:

replace_nth(text, int, old, new)
Example:
n:         2
oldValue: 'a'
newValue: 'o'
"Vader said: No, I am your father!" -> "Vader soid: No, I am your fother!"
  1     2          3        4       -> 2nd and 4th occurence are replaced
Your method has to be case sensitive!

As you can see in the example: The first changed is the 2nd 'a'. 
So the start is always at the nth suitable char and not at the first!

If n is 0 or negative or if it is larger than the count of the oldValue, 
return the original text without a change. 

"""

def replace_nth(text, n, old, new):
    if n <= 0: 
        return text
        
    i = 0
    out = []
    
    for pos, c in enumerate(text):
        if c == old:
            i += 1    
            if i % n == 0:
                out.append(new)
                continue
        out.append(c) 
        
    return ''.join(out)