def check_for_tag(player_positions):
    """
    This function checks if the tagger (Henry) is next to any other player.
    A tag counts if the player is one step away (up, down, left, or right).
    Diagonal does not count.

    Author: Fatmata Bangura
    Techniques used: conditionals, iteration, and simple logic

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


# TESTING THE FUNCTION WITH FAKE DATA
if __name__ == "__main__":
    # Fake player positions on a 4x4 grid
    sample_players = {
        "Henry": (1, 1),   # Tagger
        "Maya": (1, 2),    # Right next to Henry (should get tagged)
        "Ruth": (3, 3),    # Far away
        "Jake": (0, 0)     # Also far away
    }

    result = check_for_tag(sample_players)
    print("Result:", result)

