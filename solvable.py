def check_if_solvable(game_state):
    steps = len(game_state)
    inversion_counter = 0
    # i = number currently looking at
    for i in range(steps):
        # j = numbers that come after i
        for j in range(i + 1, steps):
            if game_state[i] > game_state[j] and not 0:
                inversion_counter += 1
    print("inv_count: " + str(inversion_counter))

  # This is checking if the number of inversions is even or odd. If it is even, then the puzzle is
  # solvable. If it is odd, then the puzzle is not solvable.
    return inversion_counter % 2 == 0
    
