class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(nums,target):
            l,r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
            return False
        
        def binarysearchBoundary(nums,target):
            l,r = 0, len(nums)-1
            print(nums)
            while l<r:
                mid = (l+r+1)//2
                # print("mid",mid)
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r = mid-1
                else:
                    l = mid
                # print("lr",l,r)
            return l
        
        b = binarysearchBoundary([m[0] for m in matrix],target)
        print(b)

        return binarysearch(matrix[b],target)
        