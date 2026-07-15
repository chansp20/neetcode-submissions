class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = {index : value for index,value in enumerate(nums)}
        i = 0
        Output = []
        for i in range(len(nums)):
            val=d.pop(i)
            k=1
            j=0
            for num in d.values():
                prod = num * k
                k = prod
                
                
            Output.append(k)
            
            d[i] = val
        return Output
            

        