# First function: place_players_and_hiding_spots
def place_players_and_hiding_spots(grid_size=4):
    """
    This function places players and hiding spots on a 4x4 grid.
    The grid is represented as a list of coordinates, and the function
    places players and hiding spots, ensuring no overlap.

    Args:
        grid_size (int): The size of the grid (default is 4).
    
    Returns:
        tuple: A dictionary of player names with their positions,
               and a list of hiding spot positions.
    """
    players = ["Jake", "Abraham", "Ruth", "Maya", "Sara", "Henry"]  # 6 players
    player_positions = {}
    taken_positions = []

    # Predefined positions
    position_sequence = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1)]
    for i, player in enumerate(players):
        player_positions[player] = position_sequence[i]  # Assign position from the sequence
        taken_positions.append(position_sequence[i])  # Add to taken positions

    # Assign hiding spots
    hiding_spots = [(2, 2), (3, 3), (1, 2)]
    taken_positions.extend(hiding_spots)

    return player_positions, hiding_spots


# Second function: check_for_tag
def check_for_tag(player_positions):
    """
    This function checks if the tagger (Henry) is next to any other player.
    A tag counts if the player is one step away (up, down, left, or right).
    Diagonal does not count.

    Args:
        player_positions (dict): dictionary with player names as keys and their (row, col) positions as values
    
    Returns:
        str: Name of tagged player if someone was tagged, or message saying no tag happened
    """
    tagger_name = "Henry"
    tagger_pos = player_positions.get(tagger_name)

    for name, position in player_positions.items():
        if name == tagger_name:
            continue  # Don't check tagger against themselves

        row_diff = abs(tagger_pos[0] - position[0])
        col_diff = abs(tagger_pos[1] - position[1])

        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            return f"{name} was tagged by {tagger_name}!"

    return "No tag happened."


# Game Logic: play_game
def play_game():
    grid_size = 4
    player_positions, hiding_spots = place_players_and_hiding_spots()

    print("Welcome to the Tagging Game!")
    print("Avoid being tagged by Henry (the tagger).")

    while True:
        # Display the current grid
        print("\nGrid:")
        for row in range(grid_size):
            for col in range(grid_size):
                found = False
                for player, pos in player_positions.items():
                    if pos == (row, col):
                        if player == "Henry":
                            print("T", end=" ")  # Henry is shown as 'T' for tagger
                        else:
                            print(player[0], end=" ")  # First letter of player's name
                        found = True
                        break
                if not found:
                    if (row, col) in hiding_spots:
                        print("H", end=" ")  # Hiding spot
                    else:
                        print(".", end=" ")  # Empty space
            print()  # Move to the next row

        # Ask for Maya's move
        move = input("Choose move for Maya (up/down/left/right): ").strip().lower()
        if move not in ["up", "down", "left", "right"]:
            print("Invalid input. Try again.")
            continue

        # Move Maya based on the input direction
        if move == "up":
            player_positions["Maya"] = (player_positions["Maya"][0] - 1, player_positions["Maya"][1])
        elif move == "down":
            player_positions["Maya"] = (player_positions["Maya"][0] + 1, player_positions["Maya"][1])
        elif move == "left":
            player_positions["Maya"] = (player_positions["Maya"][0], player_positions["Maya"][1] - 1)
        elif move == "right":
            player_positions["Maya"] = (player_positions["Maya"][0], player_positions["Maya"][1] + 1)

        # Check if Maya has been tagged by Henry
        result = check_for_tag(player_positions)
        if result != "No tag happened.":
            # Display final grid and the result if someone is tagged
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
            break  # End the game if someone is tagged

        print("No tag happened. Keep going!\n")


# Main logic to start the game
if __name__ == "__main__":
    play_game()
