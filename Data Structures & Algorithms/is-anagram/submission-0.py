class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = sorted(list(s))
        list2 = sorted(list(t))
        
        print(list1)
        print(list2)
        
        if list1 == list2:
            return True
        else:
            return False
        