class Solution:
    def rob(self, nums: List[int]) -> int:
        target = [-1] * len(nums)
        def dfs(i):
            if i>= len(nums):
                return 0
            elif target[i] != -1:
                return target[i]
            target[i] = max(nums[i]+dfs(i+2),dfs(i+1))
            return target[i]
        return dfs(0)
        