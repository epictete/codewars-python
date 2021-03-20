def largest_sum(arr):
    current = largest = 0

    for num in arr:
        current = max(current + num, num)
        largest = max(current, largest)

    return 0 if largest < 0 else largest
