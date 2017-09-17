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


def standard_deviation(dataset, population=False):
    """
      >>> from sample_data import data_set1 as ds
      >>> round(standard_deviation(ds), 4)
      0.6392
    """
    n = len(dataset)
    div = n if population else n - 1
    dsmean = mean(dataset)
    return ((sum([xi ** 2 for xi in dataset]) - n * dsmean ** 2) / div) ** 0.5


def coefficient_of_variation(dataset, population=False):
    """
      >>> from sample_data import data_set1 as ds
      >>> round(coefficient_of_variation(ds), 4)
      0.1146
    """
    return standard_deviation(dataset, population) / mean(dataset)


def skewness(dataset, population=False):
    """
      >>> from sample_data import data_set1 as ds
      >>> round(skewness(ds), 3)
      -0.115
    """
    m = mean(dataset)
    n = len(dataset) if population else len(dataset) - 1
    numerator = sum([(xi - m) ** 3 for xi in dataset])
    denominator =  n * standard_deviation(dataset) ** 3
    return numerator / denominator


if __name__ == '__main__':
    import doctest
    doctest.testmod()
