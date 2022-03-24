def solution(data, n):
    mainlist = []
    mainlist.extend(data)
    templist = []
    # for loop that adds every number that appears more than the size of n to templist
    for each in mainlist:
        if mainlist.count(each) > n:
            if not templist.count(each):
                templist.append(each)
    # Removes all numbers that appear in templist from mainlist
    for each in templist:
        while mainlist.count(each):
            mainlist.remove(each)
    # returns list of all numbers that did not appear more than the value of x
    return mainlist
