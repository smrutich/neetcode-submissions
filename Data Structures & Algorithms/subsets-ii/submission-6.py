class Solution:
    def count_set(self,nums):
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        return count,set(nums)

    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     count,oset = self.count_set(nums)
    #     res,temp = [[]],[]

    #     def recurse(oset):
    #         if not oset:
    #             return 
            
    #         for n in list(oset):
    #             temp.append(n)

    #             count[n]-=1
    #             if count[n]==0:
    #                 oset.remove(n)

    #             # print(n,temp,"rec",oset,count)
    #             recurse(oset)

    #             if sorted(temp) not in res:
    #                 res.append(sorted(temp.copy()))

    #             check = temp.pop()
    #             oset.add(check)
    #             count[check] += 1

    #             # print(n,"rec",oset,count)
    #         # return res
    #     recurse(oset)
    #     return res
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,temp = [[]],[]
        count,oset = self.count_set(nums)
        nums.sort()

        def recurse(index):
            if index >= len(nums):
                return 
            # print("index",index)
            
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                    
                temp.append(nums[i])

                # print(i,"temp",temp)
                res.append(temp.copy())
                # print("Result",res)

                recurse(i+1)

                check = temp.pop()
                # print("TEMP POP",temp)
        
        recurse(0)
            
        return res


            

        