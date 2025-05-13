# First function: place_players_and_hiding_spots
def place_players_and_hiding_spots(grid_size=4):
    players = ["Jake", "Abraham", "Ruth", "Maya", "Sara", "Henry"]
    player_positions = {}
    taken_positions = []

    # Predefined positions
    position_sequence = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1)]
    for i, player in enumerate(players):
        player_positions[player] = position_sequence[i]
        taken_positions.append(position_sequence[i])

    # Assign hiding spots
    hiding_spots = [(2, 2), (3, 3), (1, 2)]
    taken_positions.extend(hiding_spots)

    return player_positions, hiding_spots


# Second function: check_for_tag
def check_for_tag(player_positions):
    tagger_name = "Henry"
    tagger_pos = player_positions.get(tagger_name)

    for name, position in player_positions.items():
        if name == tagger_name:
            continue

        row_diff = abs(tagger_pos[0] - position[0])
        col_diff = abs(tagger_pos[1] - position[1])

        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            return f"{name} was tagged by {tagger_name}!"

    return "No tag happened."



def play_game():
    grid_size = 4
    player_positions, hiding_spots = place_players_and_hiding_spots()

    print("Welcome to the Tagging Game!")
    print("Avoid being tagged by Henry (the tagger).")

    while True:
    
        print("\nGrid:")
        for row in range(grid_size):
            for col in range(grid_size):
                found = False
                for player, pos in player_positions.items():
                    if pos == (row, col):
                        if player == "Henry":
                            print(".", end=" ")  
                        else:
                            print(player[0], end=" ")
                        found = True
                        break
                if not found:
                    if (row, col) in hiding_spots:
                        print("H", end=" ")
                    else:
                        print(".", end=" ")
            print()

        # Ask for Maya's move
        move = input("Choose move for Maya (up/down/left/right): ").strip().lower()
        if move not in ["up", "down", "left", "right"]:
            print("Invalid input. Try again.")
            continue

        # Calculate new Maya position
        maya_row, maya_col = player_positions["Maya"]
        if move == "up":
            new_pos = (maya_row - 1, maya_col)
        elif move == "down":
            new_pos = (maya_row + 1, maya_col)
        elif move == "left":
            new_pos = (maya_row, maya_col - 1)
        elif move == "right":
            new_pos = (maya_row, maya_col + 1)

        # Ensure Maya stays within bounds
        if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
            player_positions["Maya"] = new_pos
        else:
            print("Move out of bounds. Try again.")
            continue

        # Check if Maya has been tagged
        result = check_for_tag(player_positions)
        if result != "No tag happened.":
            
            print("\nFinal Grid:")
            for row in range(grid_size):
                for col in range(grid_size):
                    found = False
                    for player, pos in player_positions.items():
                        if pos == (row, col):
                            if player == "Henry":
                                print("T", end=" ")  
                            else:
                                print(player[0], end=" ")  
                            found = True
                            break
                    if not found:
                        if (row, col) in hiding_spots:
                            print("H", end=" ")
                        else:
                            print(".", end=" ")
                print()
            print(result)
            break

        print("No tag happened. Keep going!\n")



if __name__ == "__main__":
    play_game()