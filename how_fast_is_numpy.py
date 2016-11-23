import numpy as np
from time import time

def manual_mean(arr):
  sum = 0
  for i in xrange(arr.shape[0]):
    for j  in xrange(arr.shape[1]):
      sum += arr[i, j]
  return sum / arr.size

def numpy_mean(arr):
  return arr.mean()

def how_long(func, *args):
  t0 = time()
  result = func(*args)
  t1 = time()
  return result, t1 - t0

def test_run():
  nd1 = np.random.random((1000, 10000))

  res_manual, time_manual = how_long(manual_mean, nd1)
  res_numpy, time_numpy = how_long(numpy_mean, nd1)
  print 'Manual: {:.6f} ({:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)'.format(res_manual, time_manual, res_numpy, time_numpy)

  # make sure both give the same answer
  assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"

  speedup = time_manual / time_numpy
  print 'NumPy mean is', speedup, 'times faster than manual for loops.'

if __name__ == '__main__':
  test_run()