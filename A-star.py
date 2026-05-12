# Assignment-A2 : A* Algorithm for 8 Puzzle Problem
# Problem Statement:Solve 8 Puzzle Problem using A* Algorithm.



goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Directions for blank movement
directions = [
    [-1, 0],   # UP
    [1, 0],    # DOWN
    [0, -1],   # LEFT
    [0, 1]     # RIGHT
]


# ---------------- HEURISTIC FUNCTION ----------------
# Count misplaced tiles

def h_misplaced_tiles(state):

    misplaced = 0

    i = 0
    while i < 3:

        j = 0
        while j < 3:

            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                misplaced += 1

            j += 1

        i += 1

    return misplaced


# ---------------- FIND BLANK TILE ----------------

def find_blank(state):

    i = 0

    while i < 3:

        j = 0

        while j < 3:

            if state[i][j] == 0:
                return i, j

            j += 1

        i += 1


# ---------------- CHECK VALID MOVE ----------------

def is_valid(x, y):

    if x >= 0 and x < 3 and y >= 0 and y < 3:
        return True

    return False


# ---------------- COPY STATE ----------------

def copy_state(state):

    new_state = []

    i = 0

    while i < 3:

        row = []

        j = 0

        while j < 3:

            row.append(state[i][j])

            j += 1

        new_state.append(row)

        i += 1

    return new_state


# ---------------- CHECK STATE EQUALITY ----------------

def states_equal(state1, state2):

    i = 0

    while i < 3:

        j = 0

        while j < 3:

            if state1[i][j] != state2[i][j]:
                return False

            j += 1

        i += 1

    return True


# ---------------- CHECK VISITED ----------------

def is_visited(state, visited):

    i = 0

    while i < len(visited):

        if states_equal(state, visited[i]):
            return True

        i += 1

    return False


# ---------------- PRINT STATE ----------------

def print_state(state):

    i = 0

    while i < 3:

        print(state[i])

        i += 1

    print()


# ---------------- PRINT PATH ----------------

def print_path(path):

    i = 0

    while i < len(path):

        print("Step", i, ":")

        print_state(path[i])

        i += 1


# ---------------- MANUAL PRIORITY SELECTION ----------------

def get_lowest_f_index(open_list):

    min_index = 0

    i = 1

    while i < len(open_list):

        if open_list[i][0] < open_list[min_index][0]:
            min_index = i

        i += 1

    return min_index


# ---------------- A* ALGORITHM ----------------

def a_star(start_state):

    open_list = []
    visited = []

    g = 0
    h = h_misplaced_tiles(start_state)
    f = g + h

    # Store as [f, g, state, path]
    open_list.append([f, g, start_state, []])

    while len(open_list) > 0:

        # Get lowest f value manually
        min_index = get_lowest_f_index(open_list)

        current_node = open_list[min_index]

        # Remove manually
        open_list.pop(min_index)

        f = current_node[0]
        g = current_node[1]
        current = current_node[2]
        path = current_node[3]

        if is_visited(current, visited):
            continue

        visited.append(current)

        # Goal Check
        if states_equal(current, goal_state):

            final_path = path + [current]
            return final_path

        # Find blank tile
        x, y = find_blank(current)

        # Generate children
        i = 0

        while i < len(directions):

            dx = directions[i][0]
            dy = directions[i][1]

            nx = x + dx
            ny = y + dy

            if is_valid(nx, ny):

                new_state = copy_state(current)

                # Swap blank tile
                temp = new_state[x][y]
                new_state[x][y] = new_state[nx][ny]
                new_state[nx][ny] = temp

                if not is_visited(new_state, visited):

                    new_g = g + 1
                    new_h = h_misplaced_tiles(new_state)
                    new_f = new_g + new_h

                    new_path = path + [current]

                    open_list.append([new_f, new_g, new_state, new_path])

            i += 1

    return None


# ---------------- INPUT STATE ----------------

def get_input_state():

    state = []

    print("\nEnter Puzzle State (0 for blank tile):")

    i = 0

    while i < 3:

        row = input("Enter row " + str(i + 1) + ": ").split()

        temp = []

        j = 0

        while j < 3:

            temp.append(int(row[j]))
            j += 1

        state.append(temp)

        i += 1

    return state


# ---------------- DISPLAY GOAL STATE ----------------

def display_goal_state():

    print("\nGoal State:")

    print_state(goal_state)


# ---------------- MAIN MENU ----------------

def main():

    initial_state = []

    while True:

        print("\n" + "-" * 10 + " MAIN MENU " + "-" * 10)
        print("1. Enter Initial State")
        print("2. Display Goal State")
        print("3. Solve using A*")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # ENTER INITIAL STATE
        if choice == "1":

            initial_state = get_input_state()

            print("\nInitial State Saved Successfully!")

        # DISPLAY GOAL STATE
        elif choice == "2":

            display_goal_state()

        # SOLVE PUZZLE
        elif choice == "3":

            if len(initial_state) == 0:

                print("\nPlease enter initial state first!")

            else:

                solution = a_star(initial_state)

                if solution is not None:

                    print("\nSolution Found!\n")

                    print_path(solution)

                else:

                    print("\nNo Solution Found!")

        # EXIT
        elif choice == "4":

            print("\n## END OF PROGRAM ##")
            break

        else:

            print("\nInvalid Choice! Please try again.")


# DRIVER CODE
main()

# END OF CODE


'''---------- MAIN MENU ----------
1. Enter Initial State
2. Display Goal State
3. Solve using A*
4. Exit
Enter your choice: 2

Goal State:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

---------- MAIN MENU ----------
1. Enter Initial State
2. Display Goal State
3. Solve using A*
4. Exit
Enter your choice: 1

Enter Puzzle State (0 for blank tile):
Enter row 1: 1 2 3
Enter row 2: 4 0 6
Enter row 3: 7 5 8

Initial State Saved Successfully!

---------- MAIN MENU ----------
1. Enter Initial State
2. Display Goal State
3. Solve using A*
4. Exit
Enter your choice: 3

Solution Found!

Step 0 :
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 1 :
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 2 :
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

---------- MAIN MENU ----------
1. Enter Initial State
2. Display Goal State
3. Solve using A*
4. Exit
Enter your choice: 4

## END OF PROGRAM ##



What happened step by step:
Initial state had 0 (blank) in the middle at position [1][1]:
1  2  3
4  0  6
7  5  8
Step 0 → Step 1: Blank moved DOWN, 5 slid up:
1  2  3
4  5  6
7  0  8
Step 1 → Step 2: Blank moved RIGHT, 8 slid left — Goal reached:
1  2  3
4  5  6
7  8  0
Total moves = 2 (optimal solution) ✅'''