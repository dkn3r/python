f1 = open('input.txt', 'r')

data = f1.readline().split(', ')
data1 = list(data[0])
data2 = list(data[1])
del data1[0]
del data1[-1]
del data2[0]
del data2[-1]
rez2 = ''.join(data2)


def func(data1):
    a = 1
    rez1 = []
    for i in range(len(data1)-1):
        if data1[i] == data1[i+1]:
            a += 1
            if i == len(data1)-2:
                rez1.append(data1[i])
                if a != 1:
                    rez1.append(str(a))
        else:
            rez1.append(data1[i])
            if a != 1:
                rez1.append(str(a))
            a = 1
        if i == len(data1)-2 and data1[-1] != data1[-2]:
            rez1.append(data1[-1])
    if ''.join(rez1) == rez2:
        return True
    else:
        return False


print(func(data1))
