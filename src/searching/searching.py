# If target is present then return its location 
# else return -1 (not found)

def linear_search(arr, target):
    # Your code here
    # Trasverse array
    for i in range(len(arr)): 
        # locate target
        if arr[i] == target: 
            return i 

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        #   If target is greater, it's on the RHS 
        if  target > arr[mid]: 
            low = mid + 1
  
        # If target is smaller, it's on the LHS
        elif target < arr[mid] : 
            high = mid - 1
  
        # Target is mid, return it
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1
  
  
    

# Test code 
#arr = [ 3, 13, 22, 26, 40 ] 
#target = 20

#result = binary_search(arr, target) 
  
#if result != -1: 
#    print("Element is at index", str(result)) 
#else: 
#    print("Element doesn't exist in array") 
