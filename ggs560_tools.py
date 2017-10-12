#
#  Functions for GMU GGS 560 Fall 2017 Homework.
#  Doctests use values provided by examples in "Elementary Statistics for
#  Geographers, 3rd Ed." to confirm that each function computes desired
#  values. File sample_data.py contains the data used for the doctests.
#
import scipy.stats


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
    denominator = n * standard_deviation(dataset) ** 3
    return numerator / denominator


def kurtosis(dataset, population=False):
    """
    Using the kurtosis definition given in class, with
    3 subtracted from the ratio to align it with the
    normal distribution
    
      >>> from sample_data import data_set1 as ds
      >>> round(kurtosis(ds), 3)
      2.665
    """
    m = mean(dataset)
    n = len(dataset) if population else len(dataset) - 1
    numerator = sum([(xi - m) ** 4 for xi in dataset])
    denominator = n * standard_deviation(dataset) ** 4
    return (numerator / denominator) - 3


def mean_center(points):
    """
      >>> from sample_data import point_data_n_weights as pnw
      >>> points = [pnw[i][0] for i in range(len(pnw))]
      >>> x, y = mean_center(points)
      >>> round(x, 2)
      46.22
      >>> round(y, 2)
      49.56
    """
    x = sum([points[i][0] for i in range(len(points))]) / len(points)
    y = sum([points[i][1] for i in range(len(points))]) / len(points)
    return (x, y)


def weighted_mean_center(points_with_weights):
    """
      >>> from sample_data import point_data_n_weights as pnw
      >>> x, y = weighted_mean_center(pnw)
      >>> round(x, 2)
      60.34
      >>> round(y, 2)
      62.57
    """
    pnw = points_with_weights
    n = len(pnw)
    x_times_w_sum = sum([pnw[i][0][0] * pnw[i][1] for i in range(n)])
    w_sum = sum([pnw[i][1] for i in range(n)])
    x = x_times_w_sum / w_sum
    y_times_w_sum = sum([pnw[i][0][1] * pnw[i][1] for i in range(n)])
    y = y_times_w_sum / w_sum
    return (x, y)


def weighted_standard_distance(points_with_weights):
    xwmc, ywmc = weighted_mean_center(points_with_weights)
    pnw = points_with_weights
    n = len(pnw)
    wxsq = sum([pnw[i][1] * (pnw[i][0][0] - xwmc) ** 2 for i in range(n)])
    wysq = sum([pnw[i][1] * (pnw[i][0][1] - ywmc) ** 2 for i in range(n)])
    wsum = sum([pnw[i][1] for i in range(n)])
    return ((wxsq + wysq) / wsum) ** 0.5


def confidence_interval(data, percent):
    """
    Setup a test using the example from page 312 of our text.
    Needed to create some data with a standard deviation of 4.

       >>> d = [12] * 12 + [16] + [20] * 12
       >>> confidence_interval(d, 95)
       '[14.349, 17.651]'
    """
    alpha = (1 - percent / 100) / 2
    t = scipy.stats.t.ppf(1-alpha, len(data)-1)
    s = standard_deviation(data)
    error = t * s / len(data) ** 0.5
    m = mean(data)

    return '[{:0.3f}, {:0.3f}]'.format(m - error, m + error)


def confidence_interval2(mean, stddev, ds, percent):
    """
       >>> confidence_interval2(16, 4, 25, 95)
       '[14.349, 17.651]'
    """
    alpha = (1 - percent / 100) / 2
    t = scipy.stats.t.ppf(1-alpha, ds-1)
    error = t * stddev / ds ** 0.5

    return '[{:0.3f}, {:0.3f}]'.format(mean - error, mean + error)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
