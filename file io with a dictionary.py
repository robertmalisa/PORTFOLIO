players = []
with open("players.txt", "r") as file:
    for line in file:
        name, shelter = line.rstrip().split(",")
        book = {'name': name, 'shelter': shelter}
        players.append(book)

def get_shelter(shelter):
    return book['shelter']

for player in sorted(players, key=get_shelter):
    print(f"{player['name']} lives in {player['shelter']}")
