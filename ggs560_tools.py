def mean(dataset):
    """
      >>> mean([1, 2, 3])
      2.0
      >>> from sample_data import data_set1 as ds
      >>> mean(ds)
      5.58
    """
    return sum(dataset) / len(dataset)


def variance(dataset, population=False):
    """
      >>> from sample_data import data_set1 as ds
      >>> round(variance(ds), 4)
      0.4086
    """
    div = len(dataset) if population else len(dataset) - 1
    dsmean = mean(dataset)
    return sum([(xi - dsmean) ** 2 for xi in dataset]) / div 


def std_deviation(dataset, population=False):
    """
      >>> from sample_data import data_set1 as ds
      >>> round(std_deviation(ds), 4)
      0.6392
    """
    n = len(dataset)
    div = n if population else n - 1
    dsmean = mean(dataset)
    return ((sum([xi ** 2 for xi in dataset]) - n * dsmean ** 2) / div) ** 0.5


if __name__ == '__main__':
    import doctest
    doctest.testmod()
