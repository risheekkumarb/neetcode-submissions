class Solution:

    def encode(self, strs: List[str]) -> str:
        strs = [str(len(strs))] + strs
        return '|||'.join(strs)

    def decode(self, s: str) -> List[str]:
        res =  s.split('|||')
        if res[0] == 0: return []
        return res[1:]