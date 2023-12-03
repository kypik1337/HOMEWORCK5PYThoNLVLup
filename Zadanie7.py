

def is_prime(x: int):
    if x % 2 == 0 and x != 2:
        return False
    for div in range(3, int(x **0.5) + 1):
        if x % div == 0:
            return False
    return True


def prime_generator (n: int):
    for number in range(2, n + 1):
        if is_prime(number):
            yield number

print(*prime_generator(180))








