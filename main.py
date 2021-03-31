# Самый простой и неудобный
def reverse1(list):
    for i in range(1000):
        list1[i] = list[999 - i]
    print(list1)


# Быстро и удобно , но не очень понятно как работает если не знаешь про структуру
def reverse2(list):
    print(list[::-1])


# Что переписывать то
def reverse3(list: list):
    list.reverse()


if __name__ == '__main__':
    list1 = list(range(1000))
    reverse1(list1)
    reverse2(list1)
