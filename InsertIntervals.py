#given an non overlapping intervals and need to insert an interval and that should
#be also non overlapping and return final interval array
#if there is overalapping combine both intervals into one
#intervals will already be in sorted order
#categorize left non -overlapping array and right non - overlapping 

def insert_intervals(intervals, new_arr):
    n = len(intervals)
    final_arr = []
    i= 0 
    n = len(intervals)

    #left part
    #arr of end is less than start of  inserted array
    while i<n and intervals[i][1] < new_arr[0]:
        final_arr.append(intervals[i])
        i+=1
    
    #overlapping part
    # while intervals of starting [i][0] should be before ending of new interval [1]
    while i<n and intervals[i][0] <= new_arr[1]:
        new_arr[0] = min(new_arr[0],intervals[i][0])
        new_arr[1] = max(new_arr[1],intervals[i][1])
        i+=1
    final_arr.append(new_arr)

    while i<n:
        final_arr.append(intervals[i])
        i+=1
    return final_arr

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
print(insert_intervals(intervals,new_interval))


    



