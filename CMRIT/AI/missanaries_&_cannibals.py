from queue import Queue

class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left):
        # Initialize the state with the number of missionaries and cannibals on the left side,
        # and the position of the boat.
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left

    def is_valid(self):
        # Check if the state is valid:
        # - The number of cannibals doesn't exceed the number of missionaries on both sides
        # - The number of missionaries and cannibals is within the allowed range (0 to 3)
        missionaries_right = 3 - self.missionaries_left
        cannibals_right = 3 - self.cannibals_left
        return (self.missionaries_left == 0 or self.missionaries_left >= self.cannibals_left) and \
               (missionaries_right == 0 or missionaries_right >= cannibals_right) and \
               0 <= self.missionaries_left <= 3 and 0 <= self.cannibals_left <= 3

    def __eq__(self, other):
        # Define equality for states to check if two states are the same.
        return (self.missionaries_left, self.cannibals_left, self.boat_left) == \
               (other.missionaries_left, other.cannibals_left, other.boat_left)

    def __hash__(self):
        # Define hashing for states to use them in sets or dictionaries.
        return hash((self.missionaries_left, self.cannibals_left, self.boat_left))

    def __str__(self):
        # Convert state to a string for printing.
        return f"({self.missionaries_left}, {self.cannibals_left}, {self.boat_left})"

def successors(state):
    # Generate possible successor states from the given state.
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible moves: (1,0) (2,0) (0,1) (0,2) (1,1)
    possible_states = []

    for move in moves:
        dx, dy = move
        if state.boat_left:
            new_state = State(state.missionaries_left - dx, state.cannibals_left - dy, False)
        else:
            new_state = State(state.missionaries_left + dx, state.cannibals_left + dy, True)

        if new_state.is_valid():
            possible_states.append(new_state)

    return possible_states

def bfs():
    # Perform breadth-first search to find the solution.
    initial_state = State(3, 3, True)  # Start with all missionaries and cannibals on the left side.
    queue = Queue()
    queue.put([initial_state])  # Start the queue with the initial state as the first path.

    while not queue.empty():
        path = queue.get()  # Get the next path from the queue.
        current_state = path[-1]  # Get the current state from the end of the path.

        if current_state.missionaries_left == 0 and current_state.cannibals_left == 0:
            # If all missionaries and cannibals are on the right side, return the solution path.
            return path

        for next_state in successors(current_state):
            new_path = list(path)  # Create a new path by copying the current path.
            new_path.append(next_state)  # Add the next state to the new path.
            queue.put(new_path)  # Add the new path to the queue for exploration.

    return None  # If no solution is found, return None.

def print_as_list(solution):
    print("M   C   B")
    for i, state in enumerate(solution):
        missionaries_left = state.missionaries_left
        cannibals_left = state.cannibals_left
        boat_left = "L" if state.boat_left else "R"
        print(f"{missionaries_left}   {cannibals_left}   {boat_left}")

if __name__ == "__main__":
    solution = bfs()
    print_as_list(solution)

