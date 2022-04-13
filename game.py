players = []
winner = False
temp = 0
roundCount = 0


def getActivePlayer(roundCount, players):
    return players[roundCount % len(players)]


def registerPlayers(players):
    numberOfPlayers = input("With how many do you want to play? ")
    for i in range(int(numberOfPlayers)):
        players.append(input('Enter name for player {} '.format(i+1)))
    return players

players = registerPlayers(players)
matchesCount = input("With how many matches do you want to play? ")
while winner == False:
    temp = input("{}: how many matches do you want to take? (pick between 1 and 3) ".format(
        getActivePlayer(roundCount, players)))

    matchesCount = int(matchesCount) - int(temp)
    print("Rest: {}".format(matchesCount))
    temp = 0

    if matchesCount == 0:
       print("{} is the WINNER!!!".format(
           getActivePlayer(roundCount, players)))
       winner = True

    roundCount += 1
