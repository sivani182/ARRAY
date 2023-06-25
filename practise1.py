def get_subsets(arr):
    subsets = [[]]
    for i in range(len(arr)):
        for j in range(len(subsets)):
            subsets.append(subsets[j]+[arr[i]])
            
    return subsets

# example usage
my_list = [1, 2, 3]
print(get_subsets(my_list))