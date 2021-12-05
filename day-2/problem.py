if __name__ == "__main__":
    datain = open("input")
    x, y = 0, 0
    for i, e in enumerate(datain):
        all = e.split()
        direction = all[0]
        distance = int(all[1])
        if direction == "forward":
            x += distance
        if direction == "backward":
            x -= distance
        if direction == "up":
            y -= distance
        if direction == "down":
            y += distance
    print(x*y)