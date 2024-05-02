from random import uniform

p = uniform(0, 1)


def unbiased_random():
    while True:
        x = __biased_random()
        y = __biased_random()
        if x != y:
            break
    return x


def __biased_random():
    return 1 if uniform(0, 1) <= p else 0
