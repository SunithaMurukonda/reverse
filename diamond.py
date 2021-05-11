def maxDiff(arr, arr_size):
    max_diff = arr[0] - arr[1]
     
    for i in range( 0, arr_size ):
        for j in range( i+1, arr_size ):
            if(arr[i] - arr[j] > max_diff):
                max_diff = arr[i] - arr[j]
     
    return max_diff
arr = [10,11,7,12,14]
size = len(arr)
print ("Maximum difference is", maxDiff(arr, size))
