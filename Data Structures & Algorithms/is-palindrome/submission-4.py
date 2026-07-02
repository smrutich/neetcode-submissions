class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = str(s).lower().replace(' ','').replace("'",'')
        punc = set(['?',',','.',';','/',':'])

        l,r = 0, len(s)-1
        while l<=r:
            if l<r and s[l] in punc:
                l+=1
            if l<r and s[r] in punc:
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
                
        