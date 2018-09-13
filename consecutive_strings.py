"""
You are given an array strarr of strings and an integer k. 
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) 
# --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""

def longest_consec(strarr, k):
  if k <= 0 or len(strarr) == 0 or k > len(strarr):
    return ''
  long_string = ''
  
  for i in range(len(strarr) - k + 1):
    sub_str = ''.join(strarr[i:i+k])
    if len(long_string) < len(sub_str):
      long_string = sub_str
  return long_string