import sys

# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
# Printing the Output to output.txt file
# sys.stdout = open('output.txt', 'w')


def solve():
    """
        Let's rewrite concatenation in a more convenient form. ðððð(ðð,ðð)=ððâ10ðððð+ðð, where ðððð is the number of digits in ðð. Then this number is divisible by ð if and only if the sum of (ðð ððð ð) and ((ððâ10ðððð) ððð ð) is either 0 or ð.

    Let's calculate 10 arrays of remainders ððð1,ððð2,â¦,ððð10. For each ð ðð adds (ðð ððð ð) to ððððððð. That's the first term of the sum.

    Now iterate over the second term, for ðâ[1..ð] and for ðâ[1..10] you binary search for (ðâ((ððâ10ð) ððð ð)) in ðððð. The number of its occurrences should be added to answer.

    You also might have calculated some pairs (ð,ð), iterate over them and subtract them naively.

    Overall complexity: ð(10âðlogð).
    """
    n, k = map(int, sys.stdin.readline().strip().split())
    array = list(map(int, sys.stdin.readline().strip().split()))

    remainders = [{} for _ in range(11)]
    for i in range(len(array)):
        length = len(str(array[i]))
        if array[i] % k in remainders[length]:
            remainders[length][array[i] % k] += 1
        else:
            remainders[length][array[i] % k] = 1

    answer = 0
    for i in range(len(array)):
        for j in range(1, len(remainders)):
            remainder = (k - (array[i] * pow(10, j)) % k) % k
            if remainder in remainders[j]:
                answer += remainders[j][remainder]
                if len(str(array[i])) == j and ((array[i] % k) + ((array[i] * pow(10, j)) % k)) % k == 0:
                    answer -= 1
    print(answer)


if __name__ == '__main__':
    solve()
