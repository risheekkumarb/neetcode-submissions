from collections import OrderedDict, defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def _bump(self, key):
        f = self.key_to_freq[key]
        self.freq_to_keys[f].pop(key)
        if not self.freq_to_keys[f] and f == self.min_freq:
            self.min_freq += 1
        self.key_to_freq[key] = f + 1
        self.freq_to_keys[f + 1][key] = self.key_to_val[key]  # value placeholder
        self.freq_to_keys[f + 1].move_to_end(key)

    def get(self, key: int) -> int:
        if key not in self.key_to_val: return -1
        val = self.key_to_val[key]
        self.key_to_val[key] = val
        self._bump(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._bump(key)
            return
        if len(self.key_to_val) >= self.cap:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = value
        self.freq_to_keys[1].move_to_end(key)
        self.min_freq = 1
