#Define min jumps required to reach the last element
#better sort the arr by desc order so that we can attain min jumps
def JumpGame_II(arr):
    max_index = 0 #this gives the max index we can reach at every step
    end = 0 #boundary of current jump 
    jumps = 0
    n = len(arr)

    
    if n <= 1:
        return 0 #already at last index
    if arr[0] == 0:
        return -1 # cannot move forward
    
    for i in range(len(arr)):
        max_index = max(max_index, i+arr[i])

        if i == end:
            jumps+=1
            end = max_index

            if end>=n-1:
                return jumps
    return -1 #if we never reach the last index

print("The number of counts is",JumpGame_II([1, 1, 1, 1]))  # Output: 3
print("The number of counts is",JumpGame_II([2, 3, 1, 1, 4]))  # Output: 2

        

        
        
        

