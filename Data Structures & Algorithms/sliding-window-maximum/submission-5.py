class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l, r = 0, k-1
        # streak = float("-inf")
        # streak = max(nums[l:r+1])
        # res = [streak]

        # while r < len(nums)-1:
        #     print("lmr",l,r)
        #     if nums[l] < streak and nums[r+1] < streak:
        #         pass
        #     elif nums[r+1] > streak:
        #         streak = nums[r+1]
        #     elif nums[l] >= streak:
        #         streak = max(nums[l+1: r+2])
            
        #     res.append(streak)
            
        #     l += 1
        #     r += 1
        # return res
        queue = deque()
        res = []

        count = 0

        for i,n in enumerate(nums):
            # print("\n",n,"\t:",queue)
            while queue and n > nums[queue[-1]]:
                queue.pop()
                # print("pop", queue)
            queue.append(i)
            
            count += 1
            if count == k:
                res.append(nums[queue[0]])
                # print("A",res)
                if i+1-k >= queue[0]:
                    queue.popleft()
                    # print("Clean k",queue)
                count -= 1
        return res
                



  