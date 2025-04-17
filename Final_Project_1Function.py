import random

def place_random_items(grid_size, player_positions, num_items=3):
    """
    This function picks random spots on the grid to put items 
    like hiding spots or power-ups, but not where players are.

    Args:
        grid_size: a tuple like (rows, columns)
        player_positions: list of spots where players are
        num_items: how many items to place (default is 3)

    Returns:
        A list of positions where items are placed
    """

    # Step 1: Make a list of all grid positions
    all_spots = []
    for row in range(grid_size[0]):
        for col in range(grid_size[1]):
            all_spots.append((row, col))

    # Step 2: Remove player positions
    open_spots = []
    for spot in all_spots:
        if spot not in player_positions:
            open_spots.append(spot)

    # Step 3: Check if enough room
    if num_items > len(open_spots):
        print("Not enough space for items.")
        return []

    # Step 4: Pick random spots for the items
    item_spots = random.sample(open_spots, num_items)

    return item_spots


# Test the function with fake data
if __name__ == "__main__":
    grid = (5, 5)
    players = [(0, 0), (2, 2), (3, 4)]
    items = place_random_items(grid, players, 3)
    print("Items placed at:", items)
