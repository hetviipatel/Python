# You are given list containing n distinct numbers in sequence. In this list, one number is missing. 
# Write a program to find the missing value from the given n sequence numbers of list.
def find_missing_num(num_list):
    n = max(num_list)
    total_sum = 0
    num_list.sort()
    print(num_list)
    start = num_list[0]
    for i in range(start, n + 1):
        if i < 0:
            continue
        total_sum = total_sum + i
        print(total_sum)
    actual_sum = 0
    for j in num_list:
        if j < 0:
            continue
        actual_sum = actual_sum + j
        print(actual_sum)

    missing_num = total_sum - actual_sum
    return missing_num


num_list = [1, 2, -1]
missing_num = find_missing_num(num_list)
print("missing number is =", missing_num)
