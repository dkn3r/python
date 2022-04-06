f1 = open('input.txt', 'r')

data = f1.readline().split()
f1.close()

data1 = list(data[0])
data2 = list(data[1])
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def d2(data2): #this function makes the numbers in the list "4", "2", "3" (for example) the number "423"
    numb = ''
    new_data2 = []
    for j in range(len(data2)-1):
        if data2[j] not in numbers:
            new_data2.append(data2[j])
        else:
            numb += data2[j]
            if data2[j+1] not in numbers:
                new_data2.append(numb)
                numb = ''
            if j == len(data2)-1:
                new_data2.append(numb)
                numb = ''
    numb = ''
    new_data2_str = ''.join(new_data2)
    if len(data2) != len(new_data2_str):
        for q in range(len(new_data2_str), len(data2)):
            numb += data2[q]
    new_data2.append(numb)
    return new_data2

def func(data1): #this function counts the number of characters (for example: AAAA - A4) 
                 #and checks whether we are satisfied with the input data
    new_data2 = d2(data2)
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

        if len(rez1) >= 2 and data1[i+1] not in numbers:
            for y in range(len(rez1)):
                if rez1[y] != new_data2[y]:
                    return False
        if ''.join(rez1) == ''.join(new_data2):
            return True

print(func(data1))
