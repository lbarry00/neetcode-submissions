class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i, p in enumerate(position):
            cars.append((p, speed[i]))
        cars.sort(key=lambda car: car[0], reverse=True)
        
        fleets = deque()
        for car in cars:
            # car[0] = pos, car[1] = speed
            time_needed = (target - car[0]) / car[1]
            if not fleets or time_needed > fleets[-1]:
                fleets.append(time_needed)

        return len(fleets)