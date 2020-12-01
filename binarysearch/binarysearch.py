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
        print("Found {0} at index {1}".format(array[mid], mid)) # found it!
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


