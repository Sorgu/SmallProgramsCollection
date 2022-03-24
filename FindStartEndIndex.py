def solution(l, t):
    amount = len(l)
    i = 0
    while i < amount:
        i1 = i
        num = 0
        while i1 < amount:
            num += l[i1]
            if num == t:
                return [i, i1]
            elif num > t:
                break
            i1 += 1
        i += 1
    return -1, -1
