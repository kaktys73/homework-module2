n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def password(number):
    klych = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                klych += str(i) + str(j)
    return klych

print('Введите число от 3 до 20: ')
print(password(int(input())))