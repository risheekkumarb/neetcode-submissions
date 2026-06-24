class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars = sorted([(p,s) for p,s in zip(position,speed)])
        t = 0

        print(cars)
        for p,s in cars[::-1]:
            if (target-p)/s > t:
                fleets += 1
                t = max(t, (target-p)/s)

        return fleets