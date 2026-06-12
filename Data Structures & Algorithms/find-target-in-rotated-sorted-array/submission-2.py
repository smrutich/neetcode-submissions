class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     return -1
        # l, r = 0, len(nums)-1

        # while l<=r:
        #     mid = (l+r)//2
        #     if nums[mid] == target:
        #         return mid

        #     if nums[l] <= nums[mid]:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid-1
        #         else:
        #             l = mid+1
        #     else:
        #         if nums[mid] < target <= nums[r]:
        #             l = mid+1
        #         else:
        #             r = mid-1
        # return -1
        def binary_search(target,subset):
            l,r = 0, len(subset)-1
            while l<=r:
                mid=(l+r)//2
                # print("l",l,"r",r,"min",mid)
                if subset[mid] == target:
                    return mid
                elif subset[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            print("l",l,"r",r,"min",mid)
            if nums[mid]>=nums[r]:
                l = mid+1
            else:
                r = mid
         
        check = binary_search(target,nums[l:])
        print(check)
        if check != -1:
            return check + l
        
        return binary_search(target,nums[:l])