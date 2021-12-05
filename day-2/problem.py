if __name__ == "__main__":
    datain = open("input")
    x, y = 0, 0
    for i, e in enumerate(datain):
        direction = e.split()
        print(direction[0])
        if direction[0] == "forward":
            x += int(direction[1])
        if direction[0] == "backward":
            x -= int(direction[1])
        if direction[0] == "up":
            y -= int(direction[1])
        if direction[0] == "down":
            y += int(direction[1])
    print(x*y)