def linear_search(list, item):
    for n in range(len(list)):
        if list[n] == item:
            return n
    return None

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    my_list = list(range(1, 100, 3))
    print(linear_search(my_list, 67))
    print(binary_search(my_list, 67))