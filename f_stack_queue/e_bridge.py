from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0                      # Time counter in seconds.
    bridge = deque([0] * bridge_length)  # Initialize the bridge as empty (0s).
    current_weight = 0            # Current total weight on the bridge.
    # Use deque for efficient pops from the left.
    truck_weights = deque(truck_weights)

    # While there are still trucks waiting to get on the bridge...
    while truck_weights:
        time += 1
        # Remove the truck (or 0) that has reached the end of the bridge.
        current_weight -= bridge.popleft()

        # Check if the next truck can be added to the bridge.
        if truck_weights and current_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()  # Get the next truck.
            bridge.append(truck)             # Put it on the bridge.
            current_weight += truck          # Update the total weight.
        else:
            # No truck can be added; add a placeholder 0 to represent an empty space.
            bridge.append(0)

    # After all trucks have been added, they still need time to leave the bridge.
    # Since the bridge is a queue of length bridge_length, add that many seconds.
    time += bridge_length
    return time


# Example test cases:
print(solution(2, 10, [7, 4, 5, 6]))        # Expected output: 8
print(solution(100, 100, [10]))              # Expected output: 101
# Expected output: 110
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
