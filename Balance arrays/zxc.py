f1 = open('input.txt', 'r')

read = list(map(int, f1.readline().split(', ')))  # зчитування чисел через кому
f1.close()

def func(read):
    suma_read = sum(read)

    key = True
    first_part = []
    suma_first_part = 0
    
    while key:
        
        first_part.append(read[0])
        suma_first_part += read[0]
        suma_read -= read[0]
        read.pop(0)

        if suma_first_part == suma_read: 
            key = False
            return first_part
        if len(read) == 1:       
            key = False
            return False

result = func(read)
if not result:  
    print(result)
else:
    print(result, read)
    print('True')