#!/usr/bin/env python3

from sys import argv
from math import dist

def closest_pair(points):
    if len(points) < 2:
        raise ValueError('provide at least 2 points')
    it = iter(points)
    origin = next(it)

    candidates = [(dist(origin, other_point), other_point) for other_point in it]
    candidates.sort(key=lambda t : t[0])
    point_a = origin
    point_b = candidates[0][1]
    minimal_distance = candidates[0][0]

    for i in range(0, len(candidates) - 1):
        j = i + 1
        # candidates[j][0] - candidates[i][0] >= 0
        while j < len(candidates) and candidates[j][0] - candidates[i][0] < minimal_distance:
            distance = dist(candidates[i][1], candidates[j][1])
            if distance < minimal_distance:
                minimal_distance = distance
                point_a = candidates[i][1]
                point_b = candidates[j][1]
            j += 1
    return point_a, point_b

def load_data(filename):
    with open(filename, "r") as instance_file:
        points = [((float(p[0]), float(p[1]))) for p in (l.split(',') for l in instance_file)]
    return points 

def main():
    for instance in argv[1:]:
        print(closest_pair(load_data(instance)))

if __name__ == '__main__':
    main()
