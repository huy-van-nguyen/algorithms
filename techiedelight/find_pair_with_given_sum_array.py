def find_pair(numbers, target):
    dict = {}
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in dict:
            print('pair found: {} - {}'.format(diff, numbers[i]))
            return
        dict[numbers[i]] = i


if __name__ == '__main__':
    numbers = [8, 7, 2, 5, 3, 1]
    target = 10

    find_pair(numbers, target)