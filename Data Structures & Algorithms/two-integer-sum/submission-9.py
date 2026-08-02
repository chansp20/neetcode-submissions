class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            val = target - nums[i]
            if val not in nums[i+1:]:
                    continue
            else:
                for j in range(i+1,len(nums)):
               
                    if nums[j] == val:
                        return[i,j]
                    