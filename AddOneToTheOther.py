# Takes two inputs and finds out the fewest operations to get to those inputs if you start with 1 and 1, and can only
# add one onto the other (x = x + y or y = x + y). For example: 1, 1 -> 2, 1 -> 2, 3 -> 5, 3. Another example: 1, 1 ->
# 1, 2 -> 1, 3 -> 4, 3.
# To be more efficient, the function checks how many times the lower of the two numbers can be subtracted from the
# higher one. For example: 5, 3 -> 2, 3 -> 2, 1 -> 1, 1.
def solution(M='', F=''):
    # try statement to check if inputs are 0, empty, or not a number
    try:
        x = int(M)
        y = int(F)
        if not x:
            raise
        elif not y:
            raise
    except:
        return "impossible"
    generations = 0
    while x != 1 or y != 1:                     # while loop that stops if x and y are 1
        if x <= 0 or y <= 0:                    # If either x or y become 0 or goes below 0, returns as impossible
            return "impossible"
        var1 = max(x,y)
        var2 = min(x,y)
        if (var2 * 2) <= var1:                  # If the lower number fits into the higher number twice or more times,
            var3 = var1 / var2                  # the formula x=x-((x/y)*y) is used to increase efficiency.
            generations += int(var3)            # In the middle of the formula, the value of var3 is added to generations
            var3 = int(var3) * var2
            var1 -= var3
        else:
            var1 = var1 - var2                  # Lowest number is subtracted from the highest number
            generations += 1
        x = var1
        y = var2
    return str(generations)
