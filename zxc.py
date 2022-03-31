f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')
inp = list(map(int, f1.readline().split(', ')))
key = True
first = [inp[0]]
del inp[0]
second = 0
while key:
    if sum(first) == sum(inp):
        first = list((map(str, first)))
        inp = list((map(str, inp)))
        f2.write('['+', '.join(first)+']')
        f2.write(' ['+', '.join(inp)+']')
        key = False
        break

    elif inp != sum(inp):
        first.append(inp[0])
        del inp[0]
        if len(inp) == 0:
            key = False
            f2.write("False")
