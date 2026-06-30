class Solution:
    global char 
    char = ";"

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))+char+str(s)
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s):
                if s[j]==char:
                    num = int(s[i:j])
                    # print(num)
                    decoded.append(s[j+1:j+1+num])
                    i = j+num+1
                    # print(decoded)
                    # print(i)
                j+=1

        return decoded
