import collections
import itertools

if __name__ == "__main__":
    datain = open("input")
    points = collections.defaultdict(int)
    for line in datain:
        arr = line.split(" -> ")
        start, end = arr[0].split(','), arr[1].split(',')
        x1, x2 = int(start[0]), int(end[0])
        y1, y2 = int(start[1]), int(end[1])
        if x1 != x2 and y1 != y2:
            continue
        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1
        all = list(itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)))
        for elem in all:
            points[elem] += 1
    print(sum([1 for x in points.values() if x >= 2]))
