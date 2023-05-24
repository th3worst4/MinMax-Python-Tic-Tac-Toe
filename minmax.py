initialPointMatrix = [[3, 2, 3], [2, 1, 2], [3, 2, 3]]

def sumDiagonal(pointMatrix, s = False):
    sum = 0
    for i in range(3):
        if not s:
            sum += pointMatrix[i][i]
        else:
            sum += pointMatrix[2-i][i]
    return sum

def changingValues(line, column, pointMatrix, firstPlay):
    if firstPlay:
        pointMatrix[line-1][column-1] = 0
    else:
        pointMatrix[line-1][column-1] = 10

def pointSum(line, column, pointMatrix):
    vectorSums = [0, 0]
    coord = (line-1, column-1)

    for i in range(3):
        vectorSums[0] += pointMatrix[line-1][i]
        vectorSums[1] += pointMatrix[i][column-1]

    if coord not in [(1, 0), (0, 1), (2, 1), (1, 2)]:
        if coord == (1, 1):
            vectorSums.append(sumDiagonal(pointMatrix))
            vectorSums.append(sumDiagonal(pointMatrix, True))
            print("case 1")
        elif coord not in [(0, 2), (2, 0)]:
            vectorSums.append(sumDiagonal(pointMatrix))
            print("case 2")
        else:
            vectorSums.append(sumDiagonal(pointMatrix, True))
            print("case 3")
    
    return vectorSums

print(pointSum(1, 3, initialPointMatrix))