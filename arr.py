# Bubble sort
def bubble_sort(element):
    marker = True
    while marker:
        marker = False
        for i in range(len(element) - 1):
            if element[i] > element[i + 1]:
                element[i], element[i + 1] = element[i + 1], element[i]
                marker = True

N = input ("Введите 5 чисел для формирования массива")
arr=N.split()

bubble_sort(arr)
print(arr)

import time
start_time = time.time()
print("-— %s seconds —-" % (time.time() - start_time))

def selection_sort(element):

    for i in range(len(element)):
        min_element = i
        for j in range(i + 1, len(element)):
            if element[j] <element[min_element]:
                min_element = j
                element[i], element[min_element] = element[min_element], element[i]

selection_sort(arr)
print(arr)

import time
start_time = time.time()
print("-— %s seconds —-" % (time.time() - start_time))

def insertion_sort(element):
# Начнем со второго элемента, так как мы предполагаем, что первый элемент отсортирован
    for i in range(1, len(element)):
        index_item = element[i]
# И сохранить ссылку на индекс предыдущего элемента
        j = i - 1
# Переместить все элементы отсортированного сегмента вперед, если они больше, чем элемент для вставки
        while j >= 0 and element[j] > index_item:
            element[j + 1] = element[j]
            j -= 1
# Вставляем элемент
            element[j + 1] = index_item

insertion_sort(arr)
print(arr)

import time
start_time = time.time()
print("-— %s seconds —-" % (time.time() - start_time))