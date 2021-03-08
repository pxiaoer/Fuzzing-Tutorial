import random


def shellsort(elems):
    sorted_elems = elems.copy()
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(sorted_elems)):
            temp = sorted_elems[i]
            j = i
            while j >= gap and sorted_elems[j - gap] > temp:
                sorted_elems[j] = sorted_elems[j - gap]
                j -= gap
            sorted_elems[j] = temp

    return sorted_elems



a=shellsort([3, 2, 1])
print(a)


a=shellsort([5, 6, 99, 7])
print(a)
print("First element:", a[0], "length:", len(a))


assert shellsort([]) == []
assert shellsort([1,1,1]) == [1,1,1]
assert shellsort([0,2,1]) == [0,1,2]
assert shellsort([0,-2,1]) == [-2,0,1]
assert shellsort([-3.6,2,1]) == [-3.6,1,2]
assert shellsort([0,2,1]) == shellsort([1,2,0])
assert shellsort([11111111111111111111111111111111111111111111111111111111,2,-999999999999999999999]) == [-999999999999999999999,2,11111111111111111111111111111111111111111111111111111111]


def random_list():
    length = random.randint(1, 10)
    elems = []
    for i in range(length):
        elems.append(random.randint(0, 100))
    return elems




for i in range(100000):
    r= random_list()
    assert shellsort(r) == sorted(r)



