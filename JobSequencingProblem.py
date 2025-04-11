#arr is tuple as it has deadline, profit, jobid
# like ("2", "100", "J1")
# arr = [[(2, 100, "J1"), (1, 50, "J2"), (2, 10, "J3"), (1, 20, "J4"), (3, 80, "J5")]

def JSP(arr):
    arr.sort(key = lambda x: x[1], reverse=True)#sorting profit values
    max_deadline = max(job[0] for job in arr) #gives the mex deadline for us to get the result array size
    result_arr= [-1] * (max_deadline+1) #gives the final expected sequence of jobs
    total_profit= 0

    for deadline, profit, job_id in arr:
        for slot in range(deadline, 0, -1):
            if result_arr[slot] == -1: #check if that slot is empty if not place on previous element
                result_arr[slot] = job_id
                total_profit += profit
                break

    return total_profit

arr = [(2, 100, "J1"), (1, 50, "J2"), (2, 10, "J3"), (1, 20, "J4"), (3, 80, "J5")]
final_profit = JSP(arr)
print("Maximum profit is",final_profit)