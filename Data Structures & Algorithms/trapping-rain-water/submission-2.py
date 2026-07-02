class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        mtrap = 0
        nums = height

        mid = nums.index(max(nums))

        while l<mid:
            r = l+1
            while r<=mid and nums[l] > nums[r]:
                r +=1
            print("point",l,r)

            for i in range(l+1,r):
                mtrap+=(nums[l]-nums[i])

            l=r
        
        r = len(nums)-1
        while r > mid:
            l = r-1
            while l>=mid and nums[r] > nums[l]:
                l-=1
            for i in range(l+1,r):
                mtrap+=(nums[r]-nums[i])
            r = l
            

        return mtrap
        