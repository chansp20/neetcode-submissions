class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        Output=[]
        for wrds in strs:
            key = "".join(sorted(wrds))
            l=[]
            if key not in d:
                l.append(wrds)

                d[key] = l
                
            elif key in d:
                d[key].append(wrds)
            
        Output = list(d.values())
        
        return Output
            

        
            
            
                
            

            
            


            

            

        