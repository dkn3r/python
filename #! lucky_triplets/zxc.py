#import time

f1 = open('input.txt', 'r')
numbers = list(map(int, f1.readline().split(', ')))
f1.close()


''' this function is for all the same numbers in the list 
    --- 0.0009884834289550781 seconds ---'''


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


''' this function is for all different numbers in the list
    --- 0.0010066032409667969 seconds --- '''


def main(numbers):
    lucky_triplets = 0
    for first in range(len(numbers)):
        for second in range(first+1, len(numbers)):
            if numbers[second] % numbers[first] == 0 and numbers[first] <= numbers[second]:
                for third in range(second+1, len(numbers)):
                    if numbers[third] % numbers[second] == 0 and numbers[second] <= numbers[third]:
                        lucky_triplets += 1
    return lucky_triplets
# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))


if all_the_same(numbers) == False:
    print(main(numbers))
else:
    print(all_the_same(numbers))
