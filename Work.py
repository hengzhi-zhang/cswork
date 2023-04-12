import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  if v == 0:
    return v
  else:
    return v + sum_series(v//k, k)

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  my_list = []
  for x in range(n+1):
    my_list.append(sum_series(x, k))

  for x in range(len(my_list)):
    if my_list[x] >= n:
      return x


#Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  my_list = []
  for x in range(n+1):
    my_list.append(sum_series(x, k))

  low = 0
  high = len(my_list) -1
  result = 0
  while high >= low:
    mid = (high + low) //2
    if my_list[mid] >= n:
      result = mid
      high = mid - 1
    else:
      low = mid + 1

  return result




def main():
  # read number of cases
  
  debug = True
  if debug:
    in_data = open('work.in')
  else:
    in_data = sys.stdin
    
  line = in_data.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = in_data.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
