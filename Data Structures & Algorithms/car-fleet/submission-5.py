class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        t=0
        fleet = 0
        for position,speed in cars:
            time = (target-position)/speed
            if time > t:
                fleet = fleet + 1
                t = time

        return fleet


        