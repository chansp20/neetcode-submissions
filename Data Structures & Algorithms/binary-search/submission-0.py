class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        def binary_search(nums,low,high,target):
            if high >= low:
                mid = (high+low)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(nums,mid+1,high,target)
                else:
                    return binary_search(nums,low,mid-1,target)
            return -1
        
        return binary_search(nums, low, high, target)