def find_missing_num(num_list):
     n = len(num_list) 
     total_sum = 0
     for i in range(1,n+2): 
           total_sum = total_sum + i
      #      print(total_sum)
     actual_sum = sum(num_list)
     missing_num = total_sum - actual_sum
     return missing_num

num_list = [2,1,3,6,4,9,5,8]
missing_num = find_missing_num(num_list)
print("missing number is=", missing_num)
