class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        H = []
        res = []

        #create frequency Dictionary
        for num in nums:
            if num not in D:
                D[num] = 1
            else:
                D[num] += 1

        #push it into a Heap
        for key in D:
            heapq.heappush(H, (-D[key] ,key))

        #pop K times
        top = 0
        while top < k:
            freq_count, freq_num = heapq.heappop(H)
            res.append(freq_num)
            top += 1
            
        return res