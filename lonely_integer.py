"""
find the lonely integer in a list of ints.
the first int in the list will be the number of ints in the sequence and
not used.

return the int that is the lone int.

"""

def lonelyInteger(arr):
    del arr[0]
     lonely_int = []
     for i in arr:
         if arr.count(i) == 1:
             lonely_int.append(i)
     for i in lonely_int:
         return i
