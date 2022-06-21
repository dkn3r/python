f1 = open('input.txt', 'r')
data = list(f1.readline())
f1.close()
def solution(data):
    size = len(data)
    for i in range(size-1):
        if data[i] == '[':
            for j in range(i,size):
                if data [j] == ']' and ((i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0)):
                    break 
                elif data [j] == ']' and ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                    return False
        elif data[i] == '{': 
            for o in range(i,size):     
                if data [o] == '}' and ((i % 2 == 0 and o % 2 != 0) or (i % 2 != 0 and o % 2 == 0)):
                    break 
                elif data [o] == '}' and ((i % 2 == 0 and o % 2 == 0) or (i % 2 != 0 and o % 2 != 0)):
                    return False
        elif data[i] == '(':
            for k in range(i,size):     
                if data [k] == ')' and ((i % 2 == 0 and k % 2 != 0) or (i % 2 != 0 and k % 2 == 0)):
                    break 
                elif data [k] == ')' and ((i % 2 == 0 and k % 2 == 0) or (i % 2 != 0 and k % 2 != 0)):
                    return False
if solution(data) == False:
    print('False')
else:
    print('True')