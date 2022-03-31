f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')


inp = list(map(str, f1.readline().split(', ')))
a1 = list(inp[0])
del a1[0]
a2 = list(inp[-1])
del a2[1]
inp[0] = ''.join(a1)
inp[-1] = ''.join(a2)
inp = list(map(int, inp))


key = True
first = [inp[0]]
del inp[0]


while key:
    if sum(first) == sum(inp):
        first = list((map(str, first)))
        inp = list((map(str, inp)))
        f2.write('['+', '.join(first)+'],')
        f2.write(' ['+', '.join(inp)+']')
        key = False
        break

    elif inp != sum(inp):
        first.append(inp[0])
        del inp[0]
        if len(inp) == 0:
            key = False
            f2.write("False")
