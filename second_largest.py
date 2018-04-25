"""
Using Set to Remove Duplicates
I started thinking as to what I would do if the problem stated that the
same number could not be the largest and second largest integers. 
In other words, they must be unique values.

One could obviously just iterate through the list until the largest two 
unique integers are found. However, 
I immediately thought of set in Python, 
which is guaranteed to only contain unique values. 
We could create a set from the list, which would remove duplicates. 
We could then find the two maximum values in the set using the max function.

Notice I changed the list of integers to include 39 twice, but based on 
the new assumption 39 cannot be both the largest and second largest integers 
in the list. The values must be unique, 
and set will eliminate redundant values for me.

integers = [1, 16, 3, 39, 26, 4, 8, 16, 39]

unique_integers = set(integers)  # set([1, 3, 4, 39, 8, 16, 26])

largest_integer = max(unique_integers)  # 39
unique_integers.remove(largest_integer)

second_largest_integer = max(unique_integers)  # 26

The use of set solves the problem of uniqueness quite nicely.

++++++++++++++++++++++++++++++++++++++++++++

Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. 
Hence, we print 5 as the runner-up score.

"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    dups_removed = set(list(arr)) # makes a set of the list with no duplicates
    largest = max(dups_removed) # find the largest int
    dups_removed.remove(largest) # remove the largest int from the set
    second = max(dups_removed) # finds the new largest int (2nd largets overall)
    print(second)

