def update_even(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            if num_list[i][j] % 2 == 0:
                num_list[i][j] = 0
    print(num_list)

num_list = [[1, 2, 3], [4, 5, 6], [7, 8]]
update_even(num_list)