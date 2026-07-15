class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        output=[]
        for num in nums:
            count = 1
            for i in range(len(nums)):
                new_num = num+1
                if new_num in nums:
                    
                    count = count+1
                    num=new_num
                    
                else:
                    break
            output.append(count) 
        if len(output) != 0:
            result = max(output)
        else:
            result = 0            
            
        return result