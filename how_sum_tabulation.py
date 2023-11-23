# goal is to check if you using values from nums can have 'target_sum' (you can use how many times you must those values)

def how_sum_tabulation(target_sum,nums):
    array_of_sum_options = [[] for _ in range(target_sum+(max(nums)))]
    for i in nums:
        array_of_sum_options[i].append(i)
        for number in nums:
            if len(array_of_sum_options[i])>0:
                array_of_sum_options[i+number].append([i,number])
                               
    return array_of_sum_options[target_sum] if len(array_of_sum_options[target_sum])>0 else None
  

print(how_sum_tabulation(7,[5,4,3]))
print(how_sum_tabulation(7,[2,3]))
print(how_sum_tabulation(7,[2,4]))
print(how_sum_tabulation(9,[5,4]))
