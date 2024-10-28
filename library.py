# Jonathan Lee
# Purpose: Library function

def updateTopPlayers(playerName, attempts, quit_game=False):
    if quit_game:
        return

    try:
        # Open topPlayers.txt file in read mode.
        with open("topPlayers.txt", "r") as file:
            # read top players' info line by line
            players = [line.strip().split() for line in file.readlines()]
        # Add new entry to existing list.
        players.append([str(attempts), playerName])
        # Sort scores by ascending order
        players.sort(key=lambda x: int(x[0]))
        # Retain top 5 players' scores only.
        top_players = players[:5]

        # open "topPlayers.txt" file in writing mode.
        with open("topPlayers.txt", "w") as file:
            # update list.
            for player in top_players:
                file.write(f"{player[0]} {player[1]}\n")
    except FileNotFoundError:
        # write new file
        with open("topPlayers.txt", "w") as file:
            file.write(f"{attempts} {playerName}\n")

# Display the top 5 players from topPlayers.txt file
def displayTopPlayers():
    try:
        # Open topPlayers.txt file in read mode
        with open("topPlayers.txt", "r") as file:
            players = [line.strip().split() for line in file.readlines()]
        if not players:
            print(f"Current list is empty.")
        else:
            print(f"Top Players:")
            for i, player in enumerate(players):
                score, name = player
                print(f"{i + 1}. {name} : {score} attempts.")

    # Error message for no file.
    except FileNotFoundError:
        print(f"Top Players List File Not Found! Creating new file.")
    # EOF Error message
    except EOFError:
        print("An error occurred while reading the top players file.")