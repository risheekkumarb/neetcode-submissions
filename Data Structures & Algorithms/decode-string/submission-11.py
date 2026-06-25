class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        stack = []
        r = len(s) -1

        while r >= 0:
            c = s[r]
            if not stack and c.isalpha(): res.append(c)
            else:
                if c.isalpha():
                    stack[-1] = stack[-1] + c
                elif c == '[':
                    cur = stack.pop()
                    times = ''
                    while s[r-1].isdigit():
                        times += s[r-1]
                        r -= 1
                    times = int(times[::-1])
                    if len(stack) == 0:
                        res.append(times * cur[::-1])
                    else:
                        stack[-1] = stack[-1] + (times * cur)
                else:
                    stack.append('')
            r -= 1

        return ''.join(res[::-1])