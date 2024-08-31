import logic

gameMatrix = logic.initGame()

print(gameMatrix[0])
print(gameMatrix[1])
print(gameMatrix[2])
print(gameMatrix[3])

while True:
    dir = input("Type a direction u/d/l/r or press q to exit: ")
    
    if dir == "u":
        logic.shuffleUp(gameMatrix)
    elif dir == "d":
        logic.shuffleDown(gameMatrix)
    elif dir == "l":
        logic.shuffleLeft(gameMatrix)
    elif dir == "r":
        logic.shuffleRight(gameMatrix)
    elif dir == "q":
        break

    print(gameMatrix[0])
    print(gameMatrix[1])
    print(gameMatrix[2])
    print(gameMatrix[3])
    
    logic.addNumbers(gameMatrix, dir)
    logic.genNum(gameMatrix)

    print(gameMatrix[0])
    print(gameMatrix[1])
    print(gameMatrix[2])
    print(gameMatrix[3])
