class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.maps[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = self.maps.get(key,[])
        ans = ""

        l, r = 0, len(res)-1
        while l<=r:
            mid = (l+r)//2
            if res[mid][1] <= timestamp:
                ans = res[mid][0]
                l = mid+1
            else:
                r = mid-1
        return ans
        
