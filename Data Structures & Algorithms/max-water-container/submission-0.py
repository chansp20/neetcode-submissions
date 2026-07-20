class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        j = len(heights)-1
        for i in range(len(heights)):
            while i<j:
                new_area = (j-i)*min(heights[i],heights[j])
                max_area = max(area,new_area)
                area = max_area
                print(new_area)
                if heights[i]<heights[j]:
                    i = i+1
                else:
                    j=j-1


                
            return max_area

        