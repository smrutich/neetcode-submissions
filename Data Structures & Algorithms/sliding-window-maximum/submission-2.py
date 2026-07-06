class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        streak = float("-inf")
        streak = max(nums[l:r+1])
        res = [streak]

        while r < len(nums)-1:
            print("lmr",l,r)
            if nums[l] < streak and nums[r+1] < streak:
                pass
            elif nums[r+1] > streak:
                streak = nums[r+1]
            elif nums[l] >= streak:
                streak = max(nums[l+1: r+2])
            
            res.append(streak)
            
            l += 1
            r += 1
        return res


        