# Function to find a pair in an array with a given sum using hashing
def find_pair(arr, target):
    # create an empty dictionary
    d = {}
    # do for each element
    for index, element in enumerate(arr):
        # check if pair (element, target - element) exists
        # if the deference is seen before, print the pair
        diff = target - element
        if diff in d:
            print('Pair found', (diff, arr[index]))
            return
            # store index of the current element in the dictionary
        d[element] = index
    # No pair with the given sum exists in the list
    print("Pair not found")


if __name__ == '__main__':
    arr = [8, 7, 2, 5, 3, 1]
    target = 10
    find_pair(arr, target)
