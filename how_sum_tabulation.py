# goal is to check if you using values from nums can have 'target_sum' (all values can be used as many times as you wish) and what combination that would be (one is ok)

def how_sum_tabulation(target_sum, nums):
    array_of_sum_options = [None] * (target_sum + 1)
    array_of_sum_options[0] = []

    for i in range(target_sum + 1):
        if array_of_sum_options[i] is not None:
            for num in nums:
                if i + num <= target_sum:
                    new_sum_option = sorted(array_of_sum_options[i] + [num])
                    if array_of_sum_options[i + num] is None or len(new_sum_option) < len(array_of_sum_options[i + num]):
                        array_of_sum_options[i + num] = new_sum_option

    return array_of_sum_options[target_sum]


print(how_sum_tabulation(7,[5,1]))
print(how_sum_tabulation(7,[2,3]))
print(how_sum_tabulation(7,[2,4]))
print(how_sum_tabulation(100,[15,5]))