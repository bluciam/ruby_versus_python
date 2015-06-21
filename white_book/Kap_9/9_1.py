def count_steps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_steps(n-1) + count_steps(n-2) + count_steps(n-3)

def count_steps_DP(n, my):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        my[n] = count_steps_DP(n-1, my) + count_steps_DP(n-2, my) + \
        count_steps_DP(n-3, my)
    return my[n]

entrada = ''
while True:
    entrada = int(raw_input("Enter a number (30 to finish): "))
    if entrada >= 30:
        break
    my = [-1]*(entrada + 1)
#    my = [-1 for x in range(entrada + 1)]
#    print count_steps(entrada)
    print count_steps_DP(entrada, my)
    print my
    print
