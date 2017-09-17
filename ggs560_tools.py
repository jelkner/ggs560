def mean(dataset):
    return sum(dataset) / len(dataset)


def variance(dataset):
    dsmean = mean(dataset)
    return sum([(xi - dsmean) ** 2 for xi in dataset]) / len(dataset)


def std_deviation(dataset):
    n = len(dataset)
    dsmean = mean(dataset)
    return ((sum([xi ** 2 for xi in dataset]) - n * dsmean ** 2) / n) ** 0.5

print(mean(ds))
print(variance(ds))
print(std_deviation(ds))
