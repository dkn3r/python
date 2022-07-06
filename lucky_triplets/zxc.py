#import time

f1 = open('input.txt', 'r')
numbers = list(map(int, f1.readline().split(', ')))
f1.close()

#start_time = time.time()

'''if all the same numbers'''

def all_the_same(numbers):
    if len(set(numbers)) == 1:
        lucky_triplets = 0
        j = 0
        n = len(numbers) - 2
        lucky_triplets = (n * (n + 1)) // 2
        while n - j != 1:
            j += 1
            lucky_triplets += ((n - j) * (n - j + 1)) // 2
        return lucky_triplets
    else:
        return False

'''if all the different numbers'''

def solution(numbers):
    count = 0
    size = len(numbers)

    cache = [0] * size
    for x in range(size):
        for y in range(x+1, size):
            if numbers[y] % numbers[x] == 0:
                cache[y] += 1
                count += cache[x]

    return count

if all_the_same(numbers) == False:
  print(solution(numbers),1)
  #print("--- %s seconds ---" % (time.time() - start_time))
else:
  print(all_the_same(numbers),2)
  #print("--- %s seconds ---" % (time.time() - start_time))