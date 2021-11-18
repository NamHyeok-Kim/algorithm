import numpy
from scipy.stats import mode

a = list(map(int,input().split()))
print(numpy.mean(a), " ", numpy.median(a), " ", mode(a))