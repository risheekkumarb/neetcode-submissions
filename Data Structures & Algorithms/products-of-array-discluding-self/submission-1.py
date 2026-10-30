class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [],[]

        pre = 1
        for num in nums:
            prefix.append(pre)
            pre *= num
        
        suf = 1
        for num in nums[::-1]:
            suffix.append(suf)
            suf *= num

        res = []
        for pre,suf in zip(prefix,suffix[::-1]):
            res.append(pre * suf)
        return res