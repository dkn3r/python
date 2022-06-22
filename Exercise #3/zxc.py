f1 = open('input.txt', 'r')
data = list(f1.readline())
f1.close()


def solution(data):
    if data == data[::-1]:
        return('Yes, this word is a palindrome')
    else:
        return("No, this word isn't a palindrome")


print(solution(data))
