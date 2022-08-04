import time


def findSum(given_array):
  total = 0
  for i in given_array:
    total += i
  return total 

import time

start_time = time.time()
findSum([1,2,3,4,5,6,7,8,9,10])
print("--- %s seconds ---" % (time.time() - start_time))


  # what is the time complexity of this function?
