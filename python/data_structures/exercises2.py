def solution1(a, b, k):
    count_tiny = 0
    concat_numbers = []
    for i, j in zip(a, reversed(b)):
        temp_j = j
        count_digits = 0
        while temp_j != 0:
            temp_j = temp_j // 10
            count_digits += 1
        concat_number = i * count_digits + j
        concat_numbers.append(concat_number)
    for num in concat_numbers:
        if num < k:
            count_tiny += 1
    return count_tiny
print(solution1([1,2,3], [1,2,3], 31))

def solution(a, k):
    list_of_sums = []
    count = 0
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            list_of_sums.append(a[i] + a[j])
    for num in list_of_sums:
        if num % k == 0:
            count += 1
    return count

def solution2(a, k):
    nums = [a[i] + a[j] for i in range(len(a) - 1) for j in range(i+1, len(a)) if (a[i] + a[j]) % k == 0]
    print(nums)
    return len(nums)
print(solution2([1, 2, 3, 4, 5], 3))

def solution(a, k):
    if k == 0:
        return 0
    else:
        return len([a[i] + a[j] for i in range(len(a) - 1) for j in range(i+1, len(a)) \
            if (a[i] + a[j]) % k == 0])