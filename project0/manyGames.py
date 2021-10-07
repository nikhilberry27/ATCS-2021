games = ["spoons", "monopoly", "uno", "battleship"]
print ("Hi there! I like these games: ", games)

new_game = ''
while new_game != 'quit':
    new_game = input("What game do you like? Or type 'quit' to stop entering.")
    if new_game != 'quit':
        games.append((new_game))
print ("We like these games: ", games)