from random import randint as ri
 
# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

def sum_of_number():
    N = input("Enter N: ")
    numbers_str = [N, N+N, N+N+N]
    numbers_int = list(map(lambda x: int(x), numbers_str))
    result = sum(numbers_int)
    print(f"Sum = {result}")

sum_of_number()

# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число.
#  Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов,
#   совпадающая с введённым числом.

# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def chek_sequence():
    numbers_int = [ri(0, 10) for i in range(15)]
    print(numbers_int)
    N = [int(digit) for digit in input("Enter three-digit natural number: ")]
    count = 0
    for i in range(len(numbers_int)-3):
        if numbers_int[i:i+3] == N:
            count += 1
    print("Yes") if count > 0 else print("No")

chek_sequence()

# Задача 3. 
# Найдите все простые несократимые дроби, лежащие между 0 и 1, 
# знаменатель которых не превышает 11.

def farey( n, asc=True ):
    if asc: 
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n-1, n
    print ("%d/%d" % (a,b))
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        print ("%d/%d" % (a,b))

farey(11)