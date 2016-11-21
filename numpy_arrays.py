import numpy as np

def test_run():
  print np.array([(2,3,4), (5,6,7)])

  print np.empty(5)
  print np.empty((5,4))

  print np.ones((5,4), dtype=np.int_)

  # uniform distribution
  print np.random.random((5,4)) # same as np.random.rand(dim1, dim2)

  # Gaussian distribution (normal) 
  print np.random.normal(size=(5,4)) # mean = 0, s.d. = 1
  print np.random.normal(50, 10, size=(5,4)) # mean = 50, s.d. = 10

  # random integers
  print np.random.randint(0, 10, size=(5,4))
                                

if __name__ == '__main__':
    test_run()