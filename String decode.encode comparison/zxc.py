f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')
n = list(map(str, f1.readline()))
rez = []
a = 1

for i in range(len(n)-1):
    if i == len(n)-2:
        if n[-1] == n[-2]:
            rez.append(n[i])
            rez.append(str(a+1))
        else:
            rez.append(n[i])
            rez.append(str(a))
            rez.append(n[-1])
            rez.append('1')
    else:
        if n[i] == n[i+1]:
            a += 1
        else:
            rez.append(n[i])
            rez.append(str(a))
            a = 1

f2.write(''.join(rez))
