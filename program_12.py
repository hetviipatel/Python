# You are given a nested list of integers where each inner list may have a different length.
# Sort the elements in descending order and place the sorted values back into the nested list without changing the original structure
def sort_list_decending(num_list):
    count = 0
    for i in num_list:
        if (type(i) == list):
            count = count+1
    print(count)
    if (count ==0):
        num_list.sort(reverse=True) 
        print(num_list) 
        return num_list

    else:
    # merge all inner list into single list
        merged_list = []
        for i in num_list:
            merged_list.extend(i)
            print(merged_list)
        # sort the merged list in descending order
        merged_list.sort(reverse=True)
        print(merged_list)
        # place back into nested list structure
        index = 0
        for i in range(len(num_list)):
            for j in range(len(num_list[i])):
                num_list[i][j] = merged_list[index]
                index = index +1
        return(num_list)


num_list = [[1,5,3],[3,4],[1,2,6]]
print(sort_list_decending(num_list))  