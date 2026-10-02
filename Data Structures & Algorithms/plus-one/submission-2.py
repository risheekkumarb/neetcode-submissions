class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1: digits[i] += 1
            if digits[i] // 10 == 1:
                digits[i] = digits[i] % 10
                if i != 0: digits[i-1] += 1
                else: digits = [1] + digits
            else: break

        return digits
            