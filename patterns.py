n = 5

def patternA():
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            print("*", end="")
        print()

def patternB():
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            print(row, end=" ")
        print()

def patternC():
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print("*", end="")
        print()

def patternD():
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()

def patternE():
    for row in range(1, n + 1):
        printVal = 0 if row % 2 == 0 else 1
        for col in range(1, row + 1):
            print(printVal, end=" ")
            printVal = 0 if printVal == 1 else 1
        print()

def patternF():
    printVal = 1
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(printVal, end=" ")
            printVal += 1
        print()

def patternG():
    for row in range(1, n + 1):
        for col in range(1, n - row + 2):
            print("*", end="")
        print()

def patternH():
    for row in range(1, n + 1):
        for col in range(1, n - row + 2):
            print(n - row + 1, end=" ")
        print()

def patternI():
    for row in range(1, n + 1):
        for col in range(1, n - row + 2):
            print(col, end=" ")
        print()

def patternJ():
    for row in range(1, (2 * n)):
        colTimes = (2 * n - row) if row > n else row
        for col in range(1, colTimes + 1):
            print("*", end="")
        print()

def patternK():
    for row in range(1, n + 1):
        colTimes = row
        for space in range(1, n - colTimes + 1):
            print(" ", end="")
        for col in range(1, colTimes + 1):
            print("*", end="")
        print()

def patternL():
    for row in range(1, n + 1):
        colTimes = n - row + 1
        for space in range(1, n - colTimes + 1):
            print(" ", end="")
        for col in range(1, colTimes + 1):
            print("*", end="")
        print()

def patternM():
    for row in range(1, n + 1):
        for i in range(1, n - row + 1):
            print(" ", end="")
        for col in range(1, row * 2):
            print("*", end="")
        print()

def patternN():
    for row in range(5, 0, -1):
        for i in range(1, n - row + 1):
            print(" ", end="")
        for col in range(1, row * 2):
            print("*", end="")
        print()

def patternO():
    for row in range(1, n * 2):
        rowChange = (n * 2) - row if row > n else row
        for i in range(1, n - rowChange + 1):
            print(" ", end="")
        for col in range(1, rowChange * 2):
            print("*", end="")
        print()

def patternP():
    for row in range(1, (n * 2)):
        rowChange = (n * 2) - row if row > n else row
        for space in range(1, rowChange):
            print(" ", end="")
        for col in range(1, n - rowChange + 2):
            print("*", end=" ")
        print()


patternP()
