from random import normalvariate


def normal_distribution(mu, sigma):
    value = -1

    while abs(value - mu) > 4 * sigma:
        value = int(normalvariate(mu, sigma))

    return value
