class Solution:
    def encode(self, strs: List[str]) -> str:
        return '##,#,##'.join([str(len(strs))]+strs)

    def decode(self, s: str) -> List[str]:
        ret = s.split('##,#,##')
        if ret[0] == 0: return ''
        else: return ret[1:]