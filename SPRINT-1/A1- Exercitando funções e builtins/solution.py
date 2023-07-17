import math


def delta(a, b, c):
    return pow(b, 2) - 4 * a * c


def bhaskara(a, b, c):
    delta_result = delta(a, b, c)

    if delta_result < 0:
        return "Delta negativo"

    delta_root = round(math.sqrt(delta_result), 2)

    x1 = round((-b + delta_root) / (2 * a), 2)
    x2 = round((-b - delta_root) / (2 * a), 2)

    return f'x1={x1}, x2={x2}'


print(bhaskara(3, 10, 2))
