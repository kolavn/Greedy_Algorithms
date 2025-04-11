#focus on faster meetings ; ending faster
#sort use end time
# arr has start time, end time and position of meeting
#give the mzx no of meeting / give the sequence of positions

def max_meetings(start, end):
    count  = 0
    n = len(end)
    # meetings = sorted(zip(start,end), key = lambda x: x[1])
    #above sort is to get like: meetings = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    #another approach

    meetings = [(start[i], end[i], i) for i in range(n)]

    meetings.sort(key = lambda x: x[1])

    end_time = 0
    result_arr = [] #gives the sequennce of index
    
    for meeting in meetings:
            meeting_start, meeting_end, meeting_index = meeting
            if meeting_start > end_time:
                  end_time = meeting_end
                  result_arr.append((meeting_index))
                  count+=1
    return count,result_arr

start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
count, final_arr = max_meetings(start_times,end_times)
print("The max no. of meetings we can schedule is", count,"and they are", final_arr)