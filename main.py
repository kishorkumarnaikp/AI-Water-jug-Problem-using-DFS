# Function to solve the Water Jug Problem
def solveWaterJugProblem(capacity_jug1, capacity_jug2, desired_quantity):
    # Initialize a stack to store states to be explored
    stack = []
    # Initialize a set to keep track of visited states
    visited = set()
    # Push the initial state (both jugs empty) onto the stack
    initial_state = (0, 0)
    stack.append(initial_state)  # Initial state: both jugs empty

    # Continue searching until the stack is empty
    while stack:
        # Pop the top state from the stack
        current_state = stack.pop()
        print("Current state:", current_state)  # Print the current state

        # Check if either jug contains the desired quantity
        if current_state[0] == desired_quantity or current_state[1] == desired_quantity:
            return current_state  # Return the current state if the desired quantity is found

        # Add the current state to the set of visited states
        visited.add(current_state)

        # Generate all possible next states from the current state
        next_states = generateNextStates(current_state, capacity_jug1, capacity_jug2)

        # Iterate over the next states
        for state in next_states:
            # Add the state to the stack if it has not been visited before
            if state not in visited:
                stack.append(state)

    # If no solution is found, return "No solution found"
    return "No solution found"

# Function to generate all possible next states from a given state

def generateNextStates(state, capacity_jug1, capacity_jug2):
    # Initialize a list to store the next states
    next_states = []

    # Fill Jug 1 to its maximum capacity
    next_states.append((capacity_jug1, state[1]))

    # Fill Jug 2 to its maximum capacity
    next_states.append((state[0], capacity_jug2))

    # Empty Jug 1
    next_states.append((0, state[1]))

    # Empty Jug 2
    next_states.append((state[0], 0))

    # Pour water from Jug 1 to Jug 2
    pour_amount = min(state[0], capacity_jug2 - state[1])  # Calculate the amount of water that can be poured
    next_states.append((state[0] - pour_amount, state[1] + pour_amount))  # Update the states after pouring

    # Pour water from Jug 2 to Jug 1
    pour_amount = min(state[1], capacity_jug1 - state[0])  # Calculate the amount of water that can be poured
    next_states.append((state[0] + pour_amount, state[1] - pour_amount))  # Update the states after pouring

    # Return the list of next states
    return next_states

# Call the solveWaterJugProblem function with the given jug capacities and desired quantity
solution = solveWaterJugProblem(4, 3, 2)
# Print the solution
print("Solution:", solution)
