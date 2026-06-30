class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count = {}
        # for n in nums:
        #     count[n]= count.get(n,0)+1
        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     print(heap)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        #         print(heap)
        
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1
        
        freq = [[] for _ in range(len(nums)+1)]

        for num,v in count.items():
            freq[v].append(num)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                res.extend(freq[i])
                print(res)
                if len(res) >= k:
                    return res
            # for num in freq[i]:
            #     res.append(num)
            #     if len(res) == k:
            #         return res
        return []
