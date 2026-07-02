class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)

        streak = 0
        res = []
        for i in nums:
            if i-1 in check:
                continue
            else:
                temp = [i]
                while i+1 in check:
                    temp.append(i+1)
                    i= i+1
                if len(temp) > streak:
                    res = temp
                    streak = len(temp)
        return streak
            
        