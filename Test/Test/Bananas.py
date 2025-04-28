def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)
    result_k = high

    while low <= high:
        k = low + (high - low) // 2
        t_hours = 0
        for size in piles:
            h_for_pile = (size + k - 1) // k
            t_hours += h_for_pile

        if t_hours <= h:
            result_k = k
            high = k - 1
        else:
            low = k + 1

    return result_k

print(minEatingSpeed([7], 3))