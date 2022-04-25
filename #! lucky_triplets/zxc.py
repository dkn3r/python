import time

f1 = open('input.txt', 'r')
numbers = list(map(int, f1.readline().split(', ')))
f1.close()


# --- 0.0009884834289550781 seconds ---
''' this function is for all identical numbers in the list '''


def all_the_same(numbers):
    if len(set(numbers)) == 1:
        lucky_triplets = 0
        j = 0
        lucky_triplets = et = ((len(numbers) - 2) *
                               ((len(numbers) - 2) + 1)) // 2
        while len(numbers) - 2 - j != 1:
            j += 1
            lucky_triplets += ((len(numbers) - 2 - j) *
                               ((len(numbers)-2 - j) + 1)) // 2
        return lucky_triplets
    else:
        return False


# --- 0.0010066032409667969 seconds ---
''' this function is for all non-identical numbers in the list '''


def main(numbers):
    lucky_triplets = 0
    for first in range(len(numbers)):
        for second in range(first+1, len(numbers)):
            if numbers[second] % numbers[first] == 0:
                for third in range(second+1, len(numbers)):
                    if numbers[third] % numbers[second] == 0:
                        lucky_triplets += 1
    return lucky_triplets
# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))


if all_the_same(numbers) == False:
    print(main(numbers))
else:
    print(all_the_same(numbers))
