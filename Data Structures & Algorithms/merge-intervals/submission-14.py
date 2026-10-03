class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        
        for start,end in intervals:
            if output and start <= output[-1][1]:
                output[-1][1] = max(output[-1][1],end)
            else:
                output.append([start,end])
        
        return output
        