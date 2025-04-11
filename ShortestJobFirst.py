def SJF(arr):
    arr = sorted(arr)
    n = len(arr)
    time = 0
    waiting_time = 0

    for i in range(len(arr)):
        waiting_time = time + waiting_time
        time = time+arr[i]
    return waiting_time//n

arr = [4,3,7,1,2]
print("The average waiting time is", SJF(arr))
