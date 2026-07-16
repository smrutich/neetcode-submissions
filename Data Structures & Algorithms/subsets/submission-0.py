class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res, temp = [[]],[]

        def recurse(ind):
            if ind>=len(nums):
                return 
            print("ind",ind)
            
            for i in range(ind,len(nums)):
                temp.append(nums[i])
                print(ind,i,temp)
                recurse(i+1)
                res.append(temp.copy())
                temp.pop()
        
        recurse(0)
        return res