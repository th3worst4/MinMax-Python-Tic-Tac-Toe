initialPointMatrix = [[3, 2, 3], [2, 1, 2], [3, 2, 3]]

def sumDiagonal(initialPointMatrix, s = False):
    sum = 0
    for i in range(3):
        if not s:
            sum += initialPointMatrix[i][i]
        else:
            sum += initialPointMatrix[2-i][i]
    return sum

def pointSum(line, column):
    initialPointMatrix[line-1][column-1] = 0
    vectorSums = [0, 0]
    coord = (line-1, column-1)

    for i in range(3):
        vectorSums[0] += initialPointMatrix[line-1][i]
        vectorSums[1] += initialPointMatrix[i][column-1]

    if coord not in [(1, 0), (0, 1), (2, 1), (1, 2)]:
        if coord == (1, 1):
            vectorSums.append(sumDiagonal(initialPointMatrix))
            vectorSums.append(sumDiagonal(initialPointMatrix, True))
            print("case 1")
        elif coord not in [(0, 2), (2, 0)]:
            vectorSums.append(sumDiagonal(initialPointMatrix))
            print("case 2")
        else:
            vectorSums.append(sumDiagonal(initialPointMatrix, True))
            print("case 3")
    
    return vectorSums

print(pointSum(1, 3))