def is_prime(num):
    if num <= 1:
        return False

    max_divisor = int(num ** 0.5)

    for i in range(2, max_divisor + 1):
        if num % i == 0:
            return False

    return True
