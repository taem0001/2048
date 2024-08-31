import random


def initGame():
    matrix = [[0 for _ in range(4)] for _ in range(4)]

    row1, col1 = random.randint(0, 3), random.randint(0, 3)
    matrix[row1][col1] = 2
    
    while True:
        row2, col2 = random.randint(0, 3), random.randint(0, 3)

        if (row2, col2) != (row1, col1):
            matrix[row2][col2] = 2
            break

    return matrix


def shuffleLeft(matrix):
    for i in range(4):
        row = []
        for element in matrix[i]:
            if element != 0:
                row.append(element)
        for _ in range(4 - len(row)):
            row.append(0)
        matrix[i] = row

    return matrix


def shuffleRight(matrix):
    for i in range(4):
        row = []
        stack = []
        for element in matrix[i]:
            if element != 0:
                stack.append(element)
        for _ in range(4 - len(stack)):
            stack.append(0)
        stack = inverseList(stack)
        for _ in range(4):
            row.append(stack.pop())
        matrix[i] = row

    return matrix


def shuffleUp(matrix):
    for i in range(4):
        col = getCol(matrix, i)
        for j in range(4):
            matrix[j][i] = col[j]
    return matrix


def shuffleDown(matrix):
    for i in range(4):
        col = inverseList(getCol(matrix, i))
        k = 3
        for j in range(4):
            matrix[j][i] = col[k]
            k -= 1
    return matrix


def addNumbers(matrix, dir):
    if dir == "u":
        for i in range(4):
            for j in range(3):
                if matrix[j][i] == matrix[j + 1][i]:
                    matrix[j][i] *= 2
                    matrix[j + 1][i] = 0
    elif dir == "d":
        for i in range(4):
            for j in range(3):
                if matrix[j][i] == matrix[j + 1][i]:
                    matrix[j + 1][i] *= 2
                    matrix[j][i] = 0
    elif dir == "l":
        for i in range(4):
            for j in range(3):
                if matrix[i][j] == matrix[i][j + 1]:
                    matrix[i][j] *= 2
                    matrix[i][j + 1] = 0
    elif dir == "r":
        for i in range(4):
            for j in range(3):
                if matrix[i][j] == matrix[i][j + 1]:
                    matrix[i][j + 1] *= 2
                    matrix[i][j] = 0

    return matrix


def genNum(matrix):
    num = 2 if random.random() <= 0.95 else 4
    row, col = random.randint(0, 3), random.randint(0, 3)

    while True:
        if matrix[row][col] != 0:
            row, col = random.randint(0, 3), random.randint(0, 3)
        else:
            break

    matrix[row][col] = num
    return matrix


def getCol(matrix, i):
    col = []
    for j in range(4):
        if matrix[j][i] != 0:
            col.append(matrix[j][i])
    for _ in range(4 - len(col)):
        col.append(0)
    return col


def inverseList(col):
    col = [item for item in col if item != 0]

    p1 = 0
    p2 = len(col) - 1

    while p1 < p2:
        temp = col[p1]
        col[p1] = col[p2]
        col[p2] = temp

        p1 += 1
        p2 -= 1

    while len(col) < 4:
        col.append(0)

    return col
