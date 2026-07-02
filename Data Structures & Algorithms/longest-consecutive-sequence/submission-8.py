class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check = set(nums)

        # streak = 0
        # res = []
        # for i in nums:
        #     if i-1 in check:
        #         continue
        #     else:
        #         temp = [i]
        #         while i+1 in check:
        #             temp.append(i+1)
        #             i= i+1
        #         if len(temp) > streak:
        #             res = temp
        #             streak = len(temp)
        # return streak
        
        # if len(nums)==1:
        #     return 1
        # nums.sort()
        # streak = 0
        # check = 1
        # i = 0
        # while i < len(nums)-1:
        #     print("num",nums[i+1], nums[i])
        #     if nums[i+1] - nums[i] == 1:
        #         check+=1
        #     elif nums[i+1] - nums[i] == 0:
        #         pass
        #     else:
        #         check=1
        #     i+=1
        #     streak = max(check,streak)
        # return streak

        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
                # prin/t(mp)
        return res
            
        