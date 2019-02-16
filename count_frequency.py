def findCounts(arr, n): 
      
    # Traverse all array elements 
    i = 0
    while i<n: 
          
        # If this element is already processed, 
        # then nothing to do 
        if arr[i] <= 0: 
            i += 1
            continue
  
        # Find index corresponding to this element 
        # For example, index for 5 is 4 
        elementIndex = arr[i] - 1
  
        # If the elementIndex has an element that is not 
        # processed yet, then first store that element 
        # to arr[i] so that we don't loose anything. 
        if arr[elementIndex] > 0: 
            arr[i] = arr[elementIndex] 
  
            # After storing arr[elementIndex], change it 
            # to store initial count of 'arr[i]' 
            arr[elementIndex] = -1
              
        else: 
              
            # If this is NOT first occurrence of arr[i], 
            # then increment its count. 
            arr[elementIndex] -= 1
  
            # And initialize arr[i] as 0 means the element 
            # 'i+1' is not seen so far 
            arr[i] = 0
            i += 1
    line = 0
    print ("Below are counts of all elements") 
    for i in range(0,n): 
        if abs(arr[i]) != 0:
            print ("%d -> %d"%(i+1, abs(arr[i]))) 
            line += 1
    print line 
  
A = "87 101 108 99 111 109 101 32 116 111 32 116 104 101 32 50 48 49 49 32 78 89 85 32 80 111 108 121 32 67 83 65 87 32 67 84 70 32 101 118 101 110 116 46 32 87 101 32 104 97 118 101 32 112 108 97 110 110 101 100 32 109 97 110 121 32 99 104 97 108 108 101 110 103 101 115 32 102 111 114 32 121 111 117 32 97 110 100 32 119 101 32 104 111 112 101 32 121 111 117 32 104 97 118 101 32 102 117 110 32 115 111 108 118 105 110 103 32 116 104 101 109 32 97 108 108 46 32 84 104 101 32 107 101 121 32 102 111 114 32 116 104 105 115 32 99 104 97 108 108 101 110 103 101 32 105 115 32 99 114 121 112 116 111 103 114 97 112 104 121 46"
A = A.split(" ")
for i,k in enumerate(A):
    A[i] = int(k)
print findCounts(A,len(A))