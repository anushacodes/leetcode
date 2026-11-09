from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # arrival time -> sorted list
        # count -> array
        # end_time, sid -> min heapq

        cnt = [0] * k
        free = SortedList(range(k)) # prefills!
        busy = []   # end_time, sid -> min heapq

        # for each req:
            # free servers from busy
            # add them to free
            # find which server this req needs i % k
            # find first server avail >= preferred server -> bisect_left(figure out idx instead of sid)
            # increase cnt for that server
        # find max req cnt, return all servers with that num 
        
        for i in range(len(arrival)):
            # release free servers:
            while busy and busy[0][0] <= arrival[i]: # busy[0][0] gets end time from top (earliest finishing server)
                end_time, sid =heapq.heappop(busy)
                free.add(sid)

            # all servers busy
            if not free:
                continue

            # find next available server
            start = i % k
            idx = free.bisect_left(start) # choose idx of the server number or any greater than it
            # if idx doesn't exist (start was last num)
            if idx == len(free):
                idx = 0 # choose the first idx (circle back)
            server = free.pop(idx)

            cnt[server] += 1 # inc. cnt of usage of server

            # push new [end time, server id] into heapq
            heapq.heappush(busy, (arrival[i]+load[i], server))

        # return busiest servers
        # find max cnt, return servers with max cnt
        maxi = max(cnt)
        return [i for i in range(k) if cnt[i] == maxi]



            

            





