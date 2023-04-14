# Binary Search in Python
# Recursive Approach

# define the function
def bin_search(arr, low, high, query):
    mid = (low + high)//2

    # Check base case
    if (low <= high):
        # if the value is found at mid
        if (arr[mid] == query):
            return mid

        # check query in relation to middle of array
        elif (query < arr[mid]):
            return bin_search(arr, low, mid-1, query)
        else:
            return bin_search(arr, mid+1, high, query)
    else:
        return -1
