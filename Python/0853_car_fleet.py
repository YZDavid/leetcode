class Solution1:
    # First try, wrong solution
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        queue = []

        cars.sort()
        queue.extend(cars)
        total = 0
        while queue:
            new_queue = []
            while queue:
                car = queue.pop()
                new_position = car[0] + car[1]
                if new_position > target:
                    total += 1
                    continue
                if len(new_queue) == 0:
                    new_queue.append((new_position, car[1]))
                    continue
                if new_position < new_queue[0][0]:
                    new_queue.insert(0, (new_position, car[1]))
            queue = new_queue
        return total + len(queue)
    
soln = Solution1()
print(soln.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(soln.carFleet(10, [3], [3]))
print(soln.carFleet(100, [0,2,4], [4,2,1]))
print(soln.carFleet(10, [6,8], [3,2]))

class Solution2:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        if len(cars) == 1:
            return 1
        cars = [(position, speed, (target - position) / speed) for position, speed in cars]
        cars.sort(reverse=True)
        fleet = len(cars)
        for i in range(1, len(cars)):
            car_ahead_speed = cars[i-1][2]
            if cars[i][2] <= car_ahead_speed:
                fleet -= 1
        print(cars)
        return fleet 
    
print("SOLUTION 2")
soln = Solution2()
print(soln.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(soln.carFleet(10, [3], [3]))
print(soln.carFleet(100, [0,2,4], [4,2,1]))
print(soln.carFleet(10, [0,4,2], [2,1,3]))
