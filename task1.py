#n = input()
def task(array):
    first = 0
    last = len(array) - 1
    while (first < last) :
        mid = (first + last) // 2
        if array[mid] == '1':
            first = mid + 1
        else:
            if array[mid] == '0':
                last = mid - 1

    if array[last] == '0':
        return last
    elif array[last] == '1' and last != len(array)-1:
        return last + 1
    else:
        return 'There is no 0 '


print(task('111111111111111111111111100000000'))
#алгоритмическая сложность O(log n)
