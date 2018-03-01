import sys
import numpy as np

def distance(p1, p2):
    return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])


if __name__ == '__main__':

    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]

    R, C, F, N, B, T = [int(x) for x in (lines[0].split())]

    rides = [tuple(map(int, line.split())) for line in lines[1:]]

    # ride[6] is the original ride index
    rides = [ride + (ride_i,) for (ride_i, ride) in enumerate(rides)]

    cars = [([], (0, 0), 0) for c in range(F)]


    # order rides
    #print(R, C, F, N, B, T)

    #print(rides)

    #print(cars)


    rides = sorted(rides, key=(lambda x: x[4]))

    #print(rides)

    for (ride_i, ride) in enumerate(rides):
        # The car that can reach starting point the fastest
        earliest_available_car_i = -1
        best_available_time = -1

        for (car_i, car) in enumerate(cars):
            available_time = car[2] + distance(car[1], (ride[0], ride[1]))

            if best_available_time == -1 or available_time < best_available_time:
                best_available_time = available_time
                earliest_available_car_i = car_i

        earliest_available_car = cars[earliest_available_car_i]

        arrival_time = earliest_available_car[2] + \
            distance(earliest_available_car[1], (ride[0], ride[1])) + \
            distance((ride[0], ride[1]), (ride[2], ride[3]))

        # If errors, set < to be sure ;)
        if arrival_time <= ride[5]:
            cars[earliest_available_car_i] = (earliest_available_car[0] + [ride[6]], (ride[2], ride[3]), arrival_time)
        else:
            # Too bad, can't do this ride
            pass

    for car in cars:
        print(str(len(car[0])), ' '.join(str(r_i) for r_i in car[0]))
