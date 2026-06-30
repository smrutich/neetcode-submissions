class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashT = {}

        for s in strs:
            append = False
            count = self.counter(s)
            for k, v in hashT.items():
                if v[0] == count:
                    v[1].append(s)
                    append = True
                    break
            if append == False:
                hashT[s] = (count,[s])
            # print(hashT)
        res = []
        for v in hashT.values():
            res.append(v[1])
        return res
            

    def counter(self,s:str):
        c = {}
        for char in s:
            c[char] = c.get(char,0) + 1
        return c
        