def alternating_lists(list1, list2):
    combined_list = []
    for i in range(len(list1)):
        combined_list.append(list1[i])
        combined_list.append(list2[i])
    print(combined_list)
    return combined_list


alternating_lists(['a', 'b', 'c'], [1, 2, 3])
