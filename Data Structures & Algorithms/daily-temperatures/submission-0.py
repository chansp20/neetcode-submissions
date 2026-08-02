class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        
        for i in range(len(temperatures)):
            val = temperatures[i]
            found = False
            for j in range(i,len(temperatures)):
            
            
                if temperatures[j] > temperatures[i]:
                    days = j-i
                    found = True

                    output.append(days)
                    val = temperatures[j]
                    break
            if not found:
                output.append(0)
                
        return output
            

        