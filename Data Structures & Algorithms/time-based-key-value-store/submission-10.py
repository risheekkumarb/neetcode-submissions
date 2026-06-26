class TimeMap:

    def __init__(self):
        self.store = {} # key: value list, time list

    def set(self, key: str, value: str, timestamp: int) -> None:
        value_list, times_list = [], []
        if key in self.store:
            value_list = self.store[key]['value']
            times_list = self.store[key]['times']
        value_list.append(value)
        times_list.append(timestamp)
        self.store[key] = {'value':value_list, 'times':times_list}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ''
        times = self.store[key]['times']
        l,r = 0, len(times)-1
        
        while l < r:
            m = (l + r + 1) // 2
            if timestamp >= times[m]: l = m
            else: r = m - 1

        if times[l] > timestamp: return ''
        return self.store[key]['value'][l]