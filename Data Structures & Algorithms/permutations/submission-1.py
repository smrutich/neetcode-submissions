class Solution:
    def count_set(self,nums):
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        return count, set(nums)

    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        count, uset = self.count_set(nums)

        temp = []
        def recurssive(uset):
            for i,n in enumerate(list(uset)):
                temp.append(n)

                count[n] -= 1
                if count[n]==0:
                    uset.remove(n)
                
                # print(n,"rec",temp,uset,count)

                recurssive(uset)

                if len(temp)==len(nums):
                    res.append(temp.copy())
                    # print("Result",res)

                addS = temp.pop()
                # print("after pop",addS)
                uset.add(addS)
                count[n] += 1
            return res
        
        res = recurssive(uset)

        return res

        