class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars = sorted([(p,s) for p,s in zip(position,speed)])
        t = 0

        for p,s in cars[::-1]:
            ct = (target-p)/s
            if ct > t:
                fleets += 1
                t = ct

        return fleets