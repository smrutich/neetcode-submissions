class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n+1)
        for i in range(1,n+1):
            print(steps)
            count = 0
            for j in [1,2]:
                diff = i - j
                if diff == 0:
                    count += 1
                else:
                    count += steps[diff] 
            steps[i] = count
        print(steps)
        return steps[n]

        # RECURSIVE
        # res, temp = [], []
        
        # target = [0]*n

        # def recurse(options = [1,2]):

        #     for i in options:
        #         temp.append(i)
        #         check = sum(temp)

        #         # print("recurse",temp,i)
        #         if check==n:
        #             res.append(temp.copy())
        #             # print("res",res)
        #         elif check > n:
        #             temp.pop()
        #             return
                
        #         recurse()
        #         temp.pop()
        #         # print("pop",temp)
        # recurse()
        # return len(res)