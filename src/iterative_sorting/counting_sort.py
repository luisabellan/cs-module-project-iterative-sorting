# Python program for counting sort 
  
def convert_list_to_string(arr, separator=', '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """


    # Covert list of different type of items to string
    full_str = ''.join([str(elem) for elem in arr])
    print(full_str)
    return full_str

# sorts the given string arr[] in  
# alphabetical order 
def countSort(arr): 
    """    if type(arr) == list:
          arr = listToString(arr)
    """
    if type(arr) == list:
      #print(f"type is: {type(arr)}")
      arr = convert_list_to_string(arr)
       
        
    # The output character array that will have sorted arr 
    output = [0 for i in range(256)] 
  
    # Create a count array to store count of inidividul 
    # characters and initialize count array as 0 
    count = [0 for i in range(256)] 
  
    # For storing the resulting answer since the  
    # string is immutable 
   
    
    ans = ["" for _ in arr] 

 

   
          
              
    # Store count of each character 
    for i in arr: 
        count[ord(i)] += 1
  
    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(256): 
        count[i] += count[i-1] 
  
    # Build the output character array 
    for i in range(len(arr)): 
        output[count[ord(arr[i])]-1] = arr[i] 
        count[ord(arr[i])] -= 1
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(len(arr)): 
        ans[i] = output[i] 
    
    ans = "".join(ans)
    return ans  
  
# Test code


arr1 = "hello there"
ans = countSort(arr1) 
print(f"Array: {arr1}")
print(f"Sorted character array is: {ans}")

arr2 = "5672457345"
ans = countSort(arr2) 
print(f"Array: {arr2}")
print(f"Sorted character array is: {ans}")

arr3 = [3,23,5,2,1]
ans = countSort(arr3)
print(f"Array: {arr3}")
print(f"Sorted character array is: {ans}")

arr4 = ['3','23',5,2,1]
ans = countSort(arr4)
print(f"Array: {arr4}")
print(f"Sorted character array is: {ans}")

arr5 = ['3', 'b', 'B', '23', 'A', 'C', 5, 2, 1, "hello"]
ans = countSort(arr5)
print(f"Array: {arr5}")
print(f"Sorted character array is: {ans}")


