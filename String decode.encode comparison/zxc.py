f1 = open('input.txt', 'r')

data = f1.readline().split(', ')
data1 = list(data[0])
data2 = list(data[1])
del data1[0]
del data1[-1]
del data2[0]
del data2[-1]
data2 = ''.join(data2)

def func(data1):
    a = 1
    rez_data1 = []
    for i in range(len(data1)-1):

        if data1[i] == data1[i+1]:
            a += 1
            print(a)
        else:
            rez_data1.append(data1[i])
            if a != 1:
                rez_data1.append(str(a))
                a = 1
    
    if data1[-2] != data1[-1]:
        rez_data1.append(data1[-1])
    print(rez_data1)

    if ''.join(rez_data1) == data2:
        return True
    else:
        return False
print(func(data1))