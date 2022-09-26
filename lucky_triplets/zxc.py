f1 = open('input.txt', 'r')

array = list(map(int, f1.readline().split(', ')))
f1.close()

def solution(array):
  count = 0
  size = len(array)
  cache = [0] * size
  for x in range(size):
    for y in range(x+1, size):
      if array[y] % array[x] == 0:
        cache[y] += 1
        count += cache[x]
  return count

print(solution(array))