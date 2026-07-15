class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        Output=[]
        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            elif num not in d:
                d[num] = 1
        print(d) 
        for i in range(k):       
            max_value = max(d,key=d.get)
            d.pop(max_value)
            Output.append(max_value)
        return Output


            


        