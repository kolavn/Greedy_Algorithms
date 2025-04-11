#min no of platforms required for all the given trains marr and departure tim in station
#consider the intersection intervals, find the no. of trains intersecting --> ans
#for intersection, consider case1: before arr and after dev
#case2: before arrival and middle of arr and depart
#case3: arrival and depart are middle of other train
#case4: after arrival and after depart of other train
# but for optimal - look for clock passes by time in time passes by
# so sort acc to time, anyhow arr time will be sorted, sort depart time
#increase count for arrival and decrease count for departure

def min_plaforms(arrival, departure):
    count = 0
    n =  len(arrival)
    arrival = sorted(arrival)
    departure = sorted(departure)
    i = 0 #for arrival
    j = 0 #for departure
    count = 0
    max_count = 0

    #as arrival gets exhausted first
    while i<n:
        if arrival[i] <= departure[j]:
            count = count + 1
            i = i + 1
        else:
            count = count - 1
            j = j + 1
        max_count = max(max_count, count)

    return max_count

arrival_times = [900, 902, 904, 906, 908, 910, 912, 914]
departure_times = [915, 917, 919, 921, 923, 925, 927, 929]

print("Min no. of platforms required:", min_plaforms(arrival_times,departure_times))


        

