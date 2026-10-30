class TimeMap:

    def __init__(self):
        self.store = {} # key : (value, timestamp) ## pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key,[]).append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key,[])
        l,r   = 0, len(pairs)-1

        res = ''

        while l<=r:
            m = (l+r) // 2
            if pairs[m][1] <= timestamp:
                res = pairs[m][0]
                l = m+1
            else:
                r = m-1
    
        return res