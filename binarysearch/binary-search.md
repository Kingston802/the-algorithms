Binary Search 
--------------

Property | Value 
------------ | -------------
Average performance | O(log n) 
Worst-case performance | O(log n)
Best-case performance | O(1) 
Space Complexity | O(1)

Binary Search is a divide-and-conquer algorithm that is very simple to understand.
You probably use this all the time without even realising it!

When you look through a dictionary, you don't start at the front and go through every page until you find the word you are looking for. Instead, you might open the dictionary to roughly the middle and see something like "Orange". 
If the word you were looking for was later in the alphabet, you'd go to the second half of the dictionary and if it was earlier you'd look at the first half. This is a rudimentary binary search that you probably already knew! 

## Resources

* [CS50 - Binary Search](https://www.youtube.com/watch?v=D5SrAga1pno)
* [Abdul Bari - Iterative](https://www.youtube.com/watch?v=C2apEw9pgtw)
* [Abdul Bari - Recursive](https://www.youtube.com/watch?v=uEUXGcc2VXM)
* [Teaching Tree](http://teachingtree.co/watch/binary-search)

## Questions

* [Leetcode - Search Insert Position](https://leetcode.com/problems/search-insert-position/)
* [GeeksForGeeks - Binary Search](https://practice.geeksforgeeks.org/problems/binary-search/)
* [Leetcode - Binary Search Tag](https://leetcode.com/tag/binary-search/)

## Python Implementation

```python
exampleArray = [1,2,3,4,4,5,6,8,9,9,10]

array = sorted(exampleArray) # the array MUST be sorted for binary search to work 

x = 3 # searching for x 

# iterative 
left = 0
right = len(exampleArray)-1


while right >= left:
    # calculate the mid point by
    # adding half the length of 
    # the current array to the left 
    mid = left + ((right - left) // 2)

    if array[mid] == x:
        # found it!
        print("Found {0} at index {1}".format(array[mid], mid)) 
        exit()

    if x > array[mid]: 
        # take the right side of the array 
        left = mid + 1
        print(array[left::])
    else:
        # take the left side of the array 
        right = mid-1
        print(array[left:right])

print("Could not find the value!")

# recursive 
def rBinSearch(left, right, val):
    if left == right:
        if array[left] == val:
            return True
        else:
            return False

    else: 
        mid = (left + right)//2

        if val == array[mid]:
            return mid
        if val < array[mid]:
            return rBinSearch(left, mid-1, val)
        else 
            return rBinSearch(mid+1, right, val)
```
