number = input()
sum = 0

for i in range(len(number)-2, 0, -2):
    digit = int(number[i])*2

    if len(str(digit)) > 1:
        for i in str(digit):
            sum += int(i)
    else:
        sum += digit

if len(str(int(number[0])*2)) > 1:
    for i in str(int(number[0])*2):
        sum += int(i)
else:
    sum = int(number[0])*2+sum

for i in range(1, len(number)-1, 2):
    sum += int(number[i])

sum += int(number[len(number)-1])

if str(sum)[1] == '0' and len(number) >= 12:
    if int(number[0:1]) == 34 or int(number[0:1]) == 37:
        print('AMEX')
    elif int(number[0:1]) >= 51 and int(number[0:1]) <= 55:
        print('MASTER')
    elif int(number[0]) == 4:
        print('VISA')
else:
    print('INVALID')