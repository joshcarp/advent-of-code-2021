if __name__ == "__main__":
    datain = open("input")
    foo = [list(map(int, list(x))) for x in zip(*datain)]
    gamma = ""
    epsilon = ""
    for elem in foo:
        if sum(elem)/len(elem) > 0.5:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    result = int(gamma, 2) * int(epsilon, 2)
    print(result)