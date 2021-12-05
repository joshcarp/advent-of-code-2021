def boardFinished(board, selected):
    for row in board:
        for i, piece in enumerate(row):
            if piece not in selected.keys():
                break
            if i == len(row) - 1:
                return True
    return False


def boardScore(board, selected):
    unmarked = 0
    for row in board:
        for piece in row:
            if piece not in selected:
                unmarked += piece
    return unmarked


if __name__ == "__main__":
    datain = open("input")
    calls = datain.readline()
    guesses = [int(x) for x in calls.replace("\n", "").split(",")]
    allboards = []
    current = []
    selected = {}
    for i, e in enumerate(datain):
        if e == "\n":
            allboards.append(current)
            current = []
            continue
        current.append([int(x) for x in e.split(" ") if x != ""])
    result = None
    for i, e in enumerate(guesses):
        if result != None:
            break
        selected[e] = True
        for board in allboards:
            if boardFinished(board, selected):
                score = boardScore(board, selected)
                result = score * e
                break
    print("The solution is", result)