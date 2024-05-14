def pour(jug1, jug2, max1, max2):
    if jug1 == 0:
        return 0, jug2  # Fill jug1
    elif jug2 == max2:
        return jug1, 0  # Empty jug2
    else:
        space_left = max2 - jug2
        if jug1 <= space_left:
            return 0, jug1 + jug2  # Pour all of jug1 into jug2
        else:
            return jug1 - space_left, max2  # Pour part of jug1 into jug2

def dfs(jug1, jug2, target, max1, max2, visited):
    if (jug1, jug2) == target:
        return [(jug1, jug2)]
    
    visited.add((jug1, jug2))
    
    for action in ['fill jug1', 'fill jug2', 'empty jug1', 'empty jug2', 'pour jug1 to jug2', 'pour jug2 to jug1']:
        if action == 'fill jug1':
            new_state = (max1, jug2)
        elif action == 'fill jug2':
            new_state = (jug1, max2)
        elif action == 'empty jug1':
            new_state = (0, jug2)
        elif action == 'empty jug2':
            new_state = (jug1, 0)
        elif action == 'pour jug1 to jug2':
            new_state = pour(jug1, jug2, max1, max2)
        else:  # Pour jug2 to jug1
            new_state = pour(jug2, jug1, max2, max1)
        
        if new_state not in visited:
            path = dfs(new_state[0], new_state[1], target, max1, max2, visited)
            if path:
                return [(jug1, jug2)] + path

    return None

def solve_water_jug_problem(initial, target, max1, max2):
    visited = set()
    path = dfs(initial[0], initial[1], target, max1, max2, visited)
    if path:
        print("Solution found:")
        for state in path:
            print(state)
    else:
        print("No solution found.")

# Example usage:
initial_state = (0, 0)
target_state = (2, 0)
max_jug1 = 4
max_jug2 = 3
solve_water_jug_problem(initial_state, target_state, max_jug1, max_jug2)