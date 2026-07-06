class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        streak = float("-inf")
        res = []

        while r <= len(nums):
            streak = max(nums[l:r])
            res.append(streak)
            l += 1
            r += 1
        print(streak)
        return res


        