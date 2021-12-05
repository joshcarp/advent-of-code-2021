if __name__ == "__main__":
    datain = open("input")
    last = None
    ups = 0
    for i, e in enumerate(datain):
        this = int(e)
        if last is None:
            last = this
            continue
        if last < this:
            ups += 1
        last = this

    print("final answer:")
    print(ups)