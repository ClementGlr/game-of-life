# Display the current state of the world
def display_state(state):
    print("\n----------------------------------------------------------------------------------------")
    for row in state:
        for cell in row:
            print(" | " , cell, " | ", end='')
        print("\n----------------------------------------------------------------------------------------")

# Determine if the cell is living or dying
# 0 = dead, 1 = alive
def live_or_die(state, i, j):
    cell_state = 0
    neighbors_pos = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]
    if state[i][j] == 0:
        count_living_neighbors = 0
        for pos in neighbors_pos:
            if state[i + pos[0]][j + pos[1]] == 1:
                count_living_neighbors+=1
        if count_living_neighbors == 3:
            cell_state =  1
        else:
            cell_state =  0
    else:
        count_living_neighbors = 0
        for pos in neighbors_pos:
            if state[i + pos[0]][j + pos[1]] == 1:
                count_living_neighbors+=1
        if count_living_neighbors < 2 or count_living_neighbors > 3:
            cell_state = 0
        else:
            cell_state = 1
    return cell_state

# Compute the next state of each cell in the world
def compute_next_state(current_state):
    next_state = []

    for i in range(len(current_state)):
        new_row = []
        for j in range(len(current_state[i])):
            if(i == 0 or i == len(current_state)-1) or (j == 0 or j == len(current_state[i])-1):
                new_row.append(0)
            else:
                new_row.append(live_or_die(current_state,i,j))
        next_state.append(new_row)
    return next_state


# Main function to run the simulation
current_state = []

for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    current_state.append(row)

if __name__ == '__main__':
    current_state[1][2] = 1
    current_state[1][3] = 1
    current_state[2][3] = 1

    display_state(current_state)
    current_state = compute_next_state(current_state)
    display_state(current_state)
    current_state = compute_next_state(current_state)
    display_state(current_state)
