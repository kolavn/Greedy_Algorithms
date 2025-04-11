def JumpGame(arr):
    max_index = 0
    for i in range(len(arr)):
        if i > max_index:
            return False
        max_index = max(max_index, (i+arr[i])) #check for max index value everytime
    return True

arr = [1,2,4,1,1,0,2,5]
print(JumpGame(arr))
