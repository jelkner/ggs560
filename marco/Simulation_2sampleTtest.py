#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import numpy as np
from time import sleep

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

from numpy import zeros
from numpy.random import randint as randi
from numpy.random import random as rand

from ttest_ev import ttest_ev
from ttest_uev import ttest_uev

from numpy import mean
from numpy import var

import functools
print = functools.partial(print, end='')

from numpy import std

#start at: 4:45

smin = 10
smax = 20

# smin = 30
# smax = 40

simulatedPair_no = 10000 # set how many simulated pairs are negated
simulatedPair_no = 100
test_static = zeros(simulatedPair_no)
pvalue = zeros(simulatedPair_no)
alpha = 0.05

print(' Exp-#, X1-Size  X2-Size, Mean1  Mean2   Var1    Var2  t-statistic  p-value\n')

for i in range(0, simulatedPair_no):
    sample_size = randi(smin, smax, 2) # set the sample sizes

    x1 = rand(sample_size[1 - 1]) # uniform distribution
    x2 = rand(sample_size[2 - 1]) # uniform distribution

    t, p = ttest_ev(x1, x2)
    # [h,p2,ci,stats] = ttest2(x1, x2)
    t, p = ttest_uev(x1, x2)
#     [h,p2,ci,stats] = ttest2(x1, x2, 'Vartype','unequal')
    test_static[i] = t
    pvalue[i] = p

    # for output purpose
    o1 = len(x1)
    o2 = len(x2)
    mean1 = mean(x1)
    mean2 = mean(x2)
    var1 = var(x1)
    var2 = var(x2)
    print('%5d    %3d      %3d   %6.2f  %6.2f %6.2f  %6.3f    %6.3f %4.2e' % (i + 1, o1, o2, mean1, mean2, var1, var2, t, p))

    if p <= alpha:
        print("*\n")
    else:
        print("\n");

    if i <= 3:
        print('X1:');
        print('  '.join("{:5.2f}".format(x) for x in x1))
        print('\n');
        print('X2:');
        print('  '.join("{:5.2f}".format(x) for x in x2))
        print('\n');
        input()
    sleep(0.01)

from numpy import linspace
from matplotlib.mlab import normpdf
from matplotlib.pyplot import hist as histogram
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
from matplotlib.pyplot import xlabel
from matplotlib.pyplot import ylabel
from matplotlib.pyplot import title

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
#ax2.set_zorder(1)
ax1.set_zorder(ax2.get_zorder() + 1)
ax1.patch.set_visible(False)

#figure
#histogram
ax2.hist(test_static, color="orange")

#hold on
bin_size = 100 # for plotting only
min_xp = min(test_static)
max_xp = max(test_static)
xp = linspace(min_xp, max_xp, bin_size)
mu = mean(test_static)
sigma = std(test_static)
f = normpdf(xp, mu, sigma)
ax1.plot(xp, f, linewidth=1.5)
ax1.set_xlabel("Test Statistics (t values)")
ax1.set_ylabel("Probability density function (pdf)")
title_name = "With %d experiments, mean=%f and STD=%f" % (simulatedPair_no, mu, sigma)
title(title_name)

idx = [thing for thing in pvalue if thing <= alpha]
port = 100 * len(idx) / simulatedPair_no
print("there are %4.1f percent of the pairs show significant difference at %.4f level.\n" %(port, alpha))
show()
