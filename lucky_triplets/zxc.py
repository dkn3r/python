f1 = open('input.txt', 'r')
numbers = list(map(int, f1.readline().split(', ')))

'''def all_the_same(numbers):
    if len(set(numbers)) == 1:
        return True
    else:
        return False'''


def main(numbers):
    lucky_triplets = 0
    for first in range(len(numbers)):
        for second in range(first+1, len(numbers)):
            if numbers[second] % numbers[first] == 0:
                for third in range(second+1, len(numbers)):
                    if numbers[third] % numbers[second] == 0:
                        lucky_triplets += 1
    return lucky_triplets


#result1 = all_the_same(numbers)
result2 = main(numbers)

print(result2)
