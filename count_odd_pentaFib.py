def count_odd_pentaFib(n):
    cache = [0,1,1,2,4]
    count = 0
    if n < 1:
        return 0
    for _ in range(n-4):
        next_odd_pentaFib = cache[-1] + cache[-2] + cache[-3] + cache[-4] + cache[-5]
        cache.append(next_odd_pentaFib)
    for num in list(set(cache)):    
        if num % 2 != 0:
            count += 1
    return count


#different solutions from CodeWars
'''
def count_odd_pentaFib(n):
    return 2 * (n // 6) + [0, 1, 2, 2, 2, 2][n % 6] - (n >= 2)
'''


'''
buf = [0,1,1,2,4]
def count_odd_pentaFib(n):
    while len(buf)<=n:
        buf.append(sum(buf[-5:]))
    return len([i for i in set(buf[:n+1]) if i&1])
'''


'''
def count_odd_pentaFib(n):
    x = [0, 1, 1, 2, 4]
    while len(x)<=n:
        x += [sum(x[-5:])]
    return 0 if n==0 else sum(1 for i in set(x) if i%2)
'''


#i have no idea how this one works
'''
def count_odd_pentaFib(n):
    if n < 2:
        return n
    a, b = divmod(n, 6)
    return (a << 1) + (b > 0) + (b > 1) - 1
'''