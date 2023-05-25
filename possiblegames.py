def play():
    possibleGames = []
    symb = 1
    round = 0
    for i in range(9):
        matrix = [0,0,0,0,0,0,0,0,0]
        matrix[i] = symb
        possibleGames.append(matrix)
    
    round += 1
    nextRound(symb, possibleGames, round)

def nextRound(symb, possibleGames, round, pnt1 = 0, pnt2 = 0):
    if round == 9:
        #print(pnt1)
        #print(pnt2)
        #print(len(possibleGames))
        for i in possibleGames:
            logFile(i, 0)
        return
    else:
        symb *= -1
        newPossible = list()
        for game in possibleGames:
            for i in range(9):
                aux = list(game)
                if game[i] == 0:
                    aux[i] = symb
                    if checkVictory(organazingGame(aux), symb):
                        logFile(aux, symb)
                        """""
                        if symb == 1:
                            pnt1+=1
                        else:
                            pnt2-=1
                        """""
                        continue
                    else:
                        newPossible.append(aux)       
                else:
                    continue
        round+=1
        nextRound(symb, newPossible, round, pnt1, pnt2)

def organazingGame(game):
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    index = 0
    for i in range(3):
        for j in range(3):
            matrix[i][j] = game[index]
            index+=1
    return matrix

def checkVictory(matrix, symb):
    victory = False
    
    for i in range(3):
        sum1 = matrix[i][0] + matrix[i][1] + matrix[i][2]
        sum2 = matrix[0][i] + matrix[1][i] + matrix[2][i]
        if sum1 == symb*3 or sum2 == symb*3:
            victory = True
        else:
            continue

    sum3 = 0
    sum4 = 0  
    for j in range(3):
        sum3 += matrix[j][j]
        sum4 += matrix[2-j][j]
    if sum3 == symb*3 or sum4 == symb*3:
        victory = True

    return victory

def logFile(matrix, symb):
    f = open("logGameData.dat", "a")
    f.write(str(matrix) + " | " + str(symb) +"\n")
    f.close()

f = open("logGameData.dat", "x")
f.close()
play()