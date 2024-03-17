def time_to_target(car, dt):
    vi = car[1]
    di = car[0]
    t = (dt - di) / vi
    return t

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0: 
            return 0
        cars = sorted(list(zip(position, speed)), key=lambda t: t[0], reverse=True)
        n = len(cars)
        dt = target
        max_t = time_to_target(cars[0], dt)
        n_fleets = 1
        for i in range(1, n):
            di, vi = cars[i]
            ti = time_to_target((di, vi), dt)
            if ti > max_t:
                n_fleets += 1
                max_t = ti
        return n_fleets
        