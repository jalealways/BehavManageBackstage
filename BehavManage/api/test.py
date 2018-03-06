# coding=utf-8
def printst(st):
    def fu(func):
        def wrapper(*args):
            return st + str(func(*args))
        return wrapper
    return fu


@printst("bubble: ")
def bubble(list):
    n = len(list)
    for i in range(n):
        for k in range(i,n):
            if list[i] > list[k]:
                list[i], list[k] = list[k], list[i]
    return list


def binary_search(find, list):
    n = len(list)
    first = 0
    last = n-1
    if first < last:
        while first !=last:
            mid = first+last / 2

            if find == list[mid]:
                return 1
            elif find >list[mid]:
                first=mid
            else:
                last=mid
    return 0


@printst("insert_sort: ")
def insert_sort(li):
    for i in range(len(li)):
        for j in range(i):
            if li[i] <li[j]:
                li.insert(j, li.pop(i))
                break
    return li


@printst("select_sort: ")
def select_sort(li):
    for i in range(len(li)):
        min = i
        for k in range(i, len(li)):
            if li[k] < li[min]:
                min = k
        li[i], li[min] = li[min], li[i]
    return li


# @printst("quick_sort: ")
def quick_sort(lists):
    if len(lists) <= 1:
        return lists
    return quick_sort([i for i in lists[1:] if i <lists[0]]) + quick_sort(lists[0:1])\
           + quick_sort([k for k in lists[1:] if k>lists[0]])


class B:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = self._cls(*args, **kwargs)
        return self._instance


@B
class A:
    def __init__(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    li = [3, 5, 7, 1, 2, 4, 9, 8, 6]

    # print bubble(li)
    # print binary_search(90, bubble(li))
    #
    # a = A(12)
    # b = A(34)
    # print a is b
    print bubble(li)
    print insert_sort(li)
    print select_sort(li)
    print quick_sort(li)







