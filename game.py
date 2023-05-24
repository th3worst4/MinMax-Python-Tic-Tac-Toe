def printGame(matrix):
    print("\n  | 1 | 2 | 3 |")
    for i in range(3):
        print(str(i+1) + " | " +str(matrix[i][0]) + " | " + str(matrix[i][1]) + " | " + str(matrix[i][2]) + " |")

def checkVictory(matrix, symb, line, column):
    count = 0
    for i in range(3):
        if matrix[line-1][i] == symb:
            count += 1
        if count == 3:
            return True

    count = 0   
    for i in range(3):
        if matrix[i][column-1] == symb:
            count += 1
        if count == 3:
            return True
        
    count = 0
    for i in range(3):
        if matrix[i][i] == symb:
            count += 1
        if count == 3:
            return True
        
    count = 0
    for i in range(3):
        if matrix[i][2-i] == symb:
            count += 1
        if count == 3:
            return True

    return False

def game(firstPlay):
    waitingInput = True
    values = {True: "X", False: "O"}
    print("\n" + str(values[firstPlay]) + " you play first!")
    
    matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turnsPassed = 0
    
    while True:
        printGame(matrix)

        while True:
            line = int(input("Which line you want to play? "))
            column = int(input("Which column you want to play? "))         
            if matrix[line-1][column-1] == " ":
                break
            else:
                print("\nYou can't play there!\nChoose another place!\n")
        
        matrix[line-1][column-1] = values[firstPlay]
        
        if checkVictory(matrix, values[firstPlay], line, column):
            printGame(matrix)
            print("\n--------------\n" + str(values[firstPlay] + " win!"))
            break
        
        turnsPassed += 1
        if turnsPassed == 9:
            printGame(matrix)
            print("\nIt's a draw!")
            break

        firstPlay = not firstPlay
        print("\n--------------\n"+ str(values[firstPlay]) + " is your turn!")

def main():   
    match input("Who plays first? \n 1-X \n 2-O \n 3-Random\n"):
        case '1':
            firstPlay = True
        case '2':
            firstPlay = False
        case '3':
           import random
           firstPlay = random.randint(0,1)
        case _:
            print("Com'on")
    
    game(firstPlay)


main()