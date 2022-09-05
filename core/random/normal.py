from random import normalvariate


def normal_distribution(mu, sigma):
    value = -1

    while abs(value - mu) > 3 * sigma:
        value = int(normalvariate(mu, sigma))

    return value
