"""Pi approximation using the Leibniz series — two interleaved infinite generators."""


def odd_gen():
    odd = 1
    while True:
        yield odd
        odd += 2


def pi_series():
    odds = odd_gen()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))
