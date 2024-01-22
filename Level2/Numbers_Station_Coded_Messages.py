def solution(l, t):
    # Initialize pointers and sum
    start = 0
    end = 0
    current_sum = 0

    while end < len(l):
        # Add current element to the sum
        current_sum += l[end]

        # Adjust the start pointer if the sum exceeds the target
        while current_sum > t and start < end:
            current_sum -= l[start]
            start += 1

        # Check if the correct sequence is found
        if current_sum == t:
            return [start, end]

        # Move the end pointer forward
        end += 1

    # Return [-1, -1] if no sequence is found
    return [-1, -1]
