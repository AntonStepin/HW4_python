# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, 
# используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

import math
import random

# Функции sqrt и chudnovsky переписаны из интернета, с целью разобраться что к чему, в большей мере осознал процесс, однако, все же
# не до конца... 

def sqrt(n,one):
    floating_point_precision = 10**16
    n_float = float((n*floating_point_precision)//one)/floating_point_precision
    x = (int(floating_point_precision*math.sqrt(n_float))*one)//floating_point_precision
    n_one = n*one
    while 1:
        x_old = x
        x = (x + n_one // x)//2
        if x == x_old:
            break
    return x

def chudnovsky(one):
    k = 1
    a_k = one
    a_sum = one
    b_sum = 0
    c = 640320
    c3_over_24 = c**3//24
    while 1:
        a_k *=(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*c3_over_24
        a_sum += a_k
        b_sum += k*a_k
        k+=1
        if a_k == 0:
            break
    total = 13591409*a_sum + 545140134*b_sum
    pi = (426880*sqrt(10005*one,one)*one)//total
    return pi

def user_chudnovsky(accuracy_value):
    if type(accuracy_value) == float:
        base = 10
        i = 1
        while not base**(-i) == accuracy_value:
            i += 1
        base = base**i
        return (chudnovsky(base)/base)
    else:
        return "Your value of accuracy is not a float type"

# accuracy_value = 0.01
# print (user_chudnovsky(accuracy_value))

# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.

def no_repeat_numbers(from_value_in_lst: int, up_to_value_in_lst: int):
    if type(from_value_in_lst) == int and type(up_to_value_in_lst) == int:
        start_lst = []
        result_lst = []
        for i in range (0,10):
            start_lst.append(random.randint(from_value_in_lst,up_to_value_in_lst))
        print (f"Initial list\n{start_lst}")
        for value1 in start_lst:
            repeat = 0
            for value2 in start_lst:
                if value1 == value2:
                    repeat +=1
            if repeat < 2: 
                result_lst.append(value1)
        print(f"Result list\n{result_lst}")
    else:
        print("Functions attributes aren't integer")


# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]


def simple_multipliers(n: int):
    if type(n) != int:
        print("Attribute of function isn't integer")
        exit()
    i = 2
    result = []
    while n > i:
        if n % i == 0:
            result.append(i)
            n//=i
        else:
            i+=1
    if i == n:
        result.append(i)
    return result


# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

def rewrite_text_in_text_file(text: str):
    text = 'Before: ' + text
    with open ('text_file.txt', 'w') as text_info:
        text_info.write(text)
    with open ('text_file.txt', 'r') as text_info:
        new_text = ""
        for value in text_info:
            new_text = value
    for i in new_text:
        if i.isdigit():
            new_text = new_text.replace(str (i), "")
    new_text = new_text.replace("Before: ", "After: ")
    with open ('text_file.txt', 'a') as text_info:
        text_info.writelines(f"\n{new_text}")
        return [text, new_text]

# print(rewrite_text_in_text_file("He5llo Wor44ld 2222"))