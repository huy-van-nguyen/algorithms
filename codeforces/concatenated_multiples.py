import sys

# For getting input from input.txt file
sys.stdin = open('input.txt', 'r')
# Printing the Output to output.txt file
# sys.stdout = open('output.txt', 'w')


def solve():
    """
        Let's rewrite concatenation in a more convenient form. 𝑐𝑜𝑛𝑐(𝑎𝑖,𝑎𝑗)=𝑎𝑖⋅10𝑙𝑒𝑛𝑗+𝑎𝑗, where 𝑙𝑒𝑛𝑗 is the number of digits in 𝑎𝑗. Then this number is divisible by 𝑘 if and only if the sum of (𝑎𝑗 𝑚𝑜𝑑 𝑘) and ((𝑎𝑖⋅10𝑙𝑒𝑛𝑗) 𝑚𝑜𝑑 𝑘) is either 0 or 𝑘.

    Let's calculate 10 arrays of remainders 𝑟𝑒𝑚1,𝑟𝑒𝑚2,…,𝑟𝑒𝑚10. For each 𝑖 𝑎𝑖 adds (𝑎𝑖 𝑚𝑜𝑑 𝑘) to 𝑟𝑒𝑚𝑙𝑒𝑛𝑖. That's the first term of the sum.

    Now iterate over the second term, for 𝑖∈[1..𝑛] and for 𝑗∈[1..10] you binary search for (𝑘−((𝑎𝑖⋅10𝑗) 𝑚𝑜𝑑 𝑘)) in 𝑟𝑒𝑚𝑗. The number of its occurrences should be added to answer.

    You also might have calculated some pairs (𝑖,𝑖), iterate over them and subtract them naively.

    Overall complexity: 𝑂(10⋅𝑛log𝑛).
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
