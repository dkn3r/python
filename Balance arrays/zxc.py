f1 = open('input.txt', 'r')

read = list(map(int, f1.readline().split(', ')))  # зчитування чисел через кому


def func(read):
    key = True
    first_part = []
    while key:
        # додавання в список first_element першого елемента read
        first_part.append(read[0])
        del read[0]                # і видалення з списку read
        if sum(first_part) == sum(read):  # перевірка чи суми списків рівні
            key = False
            return first_part
        if len(read) == 1:        # це якщо перевірка пройшла до останнього елементу і не знайшла рівні суми
            key = False
            return False


result = func(read)
if result == False:  # це щоб не було квадратних дужок після False
    print(result)
else:
    print(result, read)
    print('True')
f1.close()
