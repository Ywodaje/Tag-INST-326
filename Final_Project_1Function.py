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
    # List of players, including the tagger
    players = ["Jake", "Abraham", "Ruth", "Maya", "Sara", "Henry"]  # 6 players
    player_positions = {}
    taken_positions = []

    # Assign positions for players in a sequence
    position_sequence = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1)]  # Adjust for grid size
    for i, player in enumerate(players):
        player_positions[player] = position_sequence[i]  # Assign position from the sequence
        taken_positions.append(position_sequence[i])  # Add to taken positions

    # Assign hiding spots
    hiding_spots = [(2, 2), (3, 3), (1, 2)]  
    for spot in hiding_spots:
        taken_positions.append(spot)  # Mark as taken spots

    return player_positions, hiding_spots


# Test the function
if __name__ == "__main__":
    players, hiding_spots = place_players_and_hiding_spots()

    print("Players and their positions:")
    for player, position in players.items():
        if player == "Henry":
            print(f"{player} (Tagger): {position}")
        else:
            print(f"{player} (Player): {position}")

    print("Hiding spots:")
    for spot in hiding_spots:
        print(spot)
