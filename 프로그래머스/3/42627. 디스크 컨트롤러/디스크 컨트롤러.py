import heapq
def solution(jobs):
    job_len = len(jobs)
    jobs.sort()

    time = 0
    total = 0
    
    que = []
    
    while jobs or que:
        while jobs and jobs[0][0] <= time:
            a, b = jobs.pop(0)
            heapq.heappush(que, (b,a))
            
        if not que:
            a, b = jobs.pop(0)
            heapq.heappush(que, (b,a))

        cost, start = heapq.heappop(que)
        total += max(0, time-start) + cost
        time = max(time, start) + cost
        
    return total // job_len
