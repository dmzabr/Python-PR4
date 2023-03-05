n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
print('Введите элементы первого мнодетсва: ')

first = []
second = []
final = []

for i in range(n):
    first.append(int(input()))
    
print('Введите элементы второго множетсва: ')
for i in range(n):
    second.append(int(input()))
    
    if (second[i] in first) and (second[i] not in final):
        final.append(second[i])
        
print(final)
    
