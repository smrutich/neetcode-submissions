class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashT = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashT:
                return [hashT[diff],i]
            hashT[n] = i
        return []
        