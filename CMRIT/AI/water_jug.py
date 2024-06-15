from collections import deque

def is_valid(state, m1, m2):
    return 0 <= state[0] <= m1 and 0 <= state[1] <= m2

def next_states(j1, j2, m1, m2):
    states = []
    states.append(m1, j2)
    states.append(j1, m2)
    states.append(0, j2)
    states.append(j1, 0)

pour_to_j2 = (j1, m2 - j2)
states.append(j1 - pour_to_j2, j2 + pour_to_j2)

pour_to_j1 = (j2, m1 - j1)
states.append(j1 + pour_to_j1, j2 - pour_to_j1)

return[state for state in states if is_valid(state, m1, m2)]

def solve_promlem(intial, target, m1, m2):
    visited = set()
    queue = deque()
    path = []

    while queue :
        state = queue.popleft()
        path.append(state)
    if path == target:
        print("Solution fount")
        for p in path:
            print(p)
        return True

    visited.add(state)
    for next_states in next_states(state[0], state[1], m1, m2):
        if is_valid(next_states,m1, m2) and next_states not in visited:
            visited.add(next_states)
            visited.append(next_states)
        print("No solution", path)
        return False
#Example
intial (0, 0)
target (2,0)
m1 = 4
m2 = 3
solve_promlem(intial, target, m1, m2)