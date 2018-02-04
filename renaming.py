# -*- coding: utf-8 -*-
def FileNaming(names):
    
    """
    Function for renaming filenames in a list in a way such that
    all files get unique names
    
    """
    new_dict = {}
    count_dict ={}
    for i in names:
        new_dict[i] = 0
        count_dict[i] = 1
    arr = []
    for j in range(len(names)):
        if new_dict[names[j]] == 0:
            arr.append(names[j])
            new_dict[names[j]] = 1
        else:
            temp = names[j] + '(' + str(count_dict[names[j]]) + ')'
            while(temp in arr):
                count_dict[names[j]] += 1
                temp = names[j] + '(' + str(count_dict[names[j]]) + ')'
            arr.append(temp)
            count_dict[names[j]] += 1
            count_dict[temp] = 1
            names[j] = temp
            new_dict[temp] = 1
    return arr
