# Binary Search in Python
# Iterative Approach

# define the function
def binary_search(arr, query):
    low = 0
    high = len(arr)-1

    while (low <= high):
        mid = (low+high)//2

        if (arr[mid] == query):
            return mid
        elif (query < arr[mid]):
            high = mid-1
        else:
            low = mid+1

    return -1
