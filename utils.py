def calculateWR(game, deck, wins, losses):

    """
    Calculates win rate by deck for a session of play
    game: The current game being played
    deck: listing of which deck is being played
    wins: number of games won in session
    losses: number of games lost in session
    """

    wins, losses = map(int, (wins, losses))

    totalGames = int(wins + losses)

    print(wins)
    print(totalGames)
    winRate = float(wins / totalGames)
    print(winRate)
    return str(winRate)
