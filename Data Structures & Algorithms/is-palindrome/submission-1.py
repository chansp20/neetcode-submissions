class Solution:
    def isPalindrome(self, s: str) -> bool:
        s3=list(s)
        lst=list(s)

        for i in s3:
            if not i.isalnum():
                lst.remove(i)
        s2=("".join(lst)).lower()
        lst=s2[::-1]
        print(lst)
        print(s2)
        if lst == s2:
            return True
        else:
            return False
        
                
        
        