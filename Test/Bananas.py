def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)
    result_k = high

    while low <= high:
        k = low + (high - low) // 2
        total_hours = 0
        for pile_size in piles:
            hours_for_pile = (pile_size + k - 1) // k
            total_hours += hours_for_pile

        if total_hours <= h:
            result_k = k
            high = k - 1
        else:
            low = k + 1

    return result_k

print(minEatingSpeed([12, 3, 42], 12))