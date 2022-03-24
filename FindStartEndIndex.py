# Function that takes a list of intgers, and a single intger. 
# The function attempts to find the first sequence of intgers in the list 
# that adds up to the single intger, and then return the first and last index of the sequence. 
# For example if the input is [1, 3, 8, 10], 11 then the output would be 1, 2 since 3 and 8 add up to 11.
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
