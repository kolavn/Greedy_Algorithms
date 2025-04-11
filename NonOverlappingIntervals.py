def non_overlappings(intervals):
    count  = 0
    intervals.sort(key=lambda x: x[1])

    end_time = 0
    n=len(intervals)
    
    for pair in intervals:
            pair_start, pair_end = pair
            if pair_start >= end_time:
                end_time = pair_end
                count+=1
    req_count = n - count        
    return req_count

intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]

final_count = non_overlappings(intervals)
print("The min no of non overlappping intervals are", final_count)