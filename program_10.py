def find_missing_num(num_list):
     n = len(num_list) 
     global total_sum
     total_sum = 0
     for i in range(1, n):
           total_sum = total_sum + i
     actual_sum = sum(num_list)
     missing_num = total_sum - actual_sum
     return missing_num
num_list = [1, 2, 4, 5, 6]
missing_num = find_missing_num(num_list)
print("missing number is=", missing_num)
