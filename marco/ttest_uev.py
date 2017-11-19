#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

from numpy import mean
from numpy import var
from numpy import sqrt
from numpy import cumsum as cdf
from scipy.stats import t
cdf = t.cdf

def ttest_uev(x, y):
    """
    function to calculate the test statistic and the p-values of two sample
    mean t test assuming unequal variance
    """

    mx = mean(x)
    sx = var(x)
    nx = len(x)

    my = mean(y)
    sy = var(y)
    ny = len(y)

    snx = sx / nx
    sny = sy / ny
    s2 = snx + sny
    numerator = s2 * s2
    denominator = snx * snx / (nx - 1) + sny * sny / (ny - 1)
    df = numerator / denominator

    s = sqrt(s2)
    t = (mx - my) / s
    p = 2 * cdf(-abs(t), df) # use the left side value only
    return t, p
