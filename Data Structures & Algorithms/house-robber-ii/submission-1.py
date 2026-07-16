class Solution:
    def roball(self, nums: List[int]) -> int:
        target = [-1]*len(nums)
        def recurse(i,):
            if i>= len(nums):
                return 0
            if target[i] != -1:
                return target[i]
            target[i] = max(recurse(i+1), nums[i]+recurse(i+2))
            return target[i]
        # print(target)
        return max(recurse(0),recurse(1))
    
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        return max(self.roball(nums[:-1]),self.roball(nums[1:]))
            