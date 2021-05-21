a = ['Din', 'DON', 'DAN']

temp = input()

flag = True

for i in a:
    if temp == i:
        flag = False

if flag:
    a.append(temp)
else:
    print('Он уже в списке')

print(*a)