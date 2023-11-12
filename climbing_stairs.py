def climbing_stairs(n):
    n.append(0)
    for i in range(len(n)-3,-1,-1):
        n[i] += min(n[i+1], n[i+2])

    return min(n[0], n[1])


# other solutions

'''
def climbing_stairs(cost):
    a = b = 0
    for c in cost:
        a, b = b, min(a, b) + c
    return min(a, b)
'''


'''
def climbing_stairs(cost):
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[-1], cost[-2])
'''


'''
def climbing_stairs(cost):
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[-2:])
'''


'''
def climbing_stairs(cost):
    #Your code here
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    new_list = [0] * n
    new_list[0] = cost[0]
    new_list[1] = cost[1]
    for i in range(2, n):
        new_list[i] = cost[i] + min(new_list[i-1], new_list[i-2])
        
    return min(new_list[-1], new_list[-2])
'''