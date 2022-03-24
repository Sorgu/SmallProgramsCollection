import gc

class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.counter = None

    def insert(self, data):     # Recursion function that creates the binary tree
        global counter, permacounter
        counter -= 1
        if counter:                              # If the value of the counter is above 0, a new branch will be created
            if not self.left:                    # Multiple if statements to ensure equal distribution
                self.left = Node()
                self.left.insert(data)
            elif not self.left.data:
                self.left.insert(data)
            elif not self.right:
                self.right = Node()
                self.right.insert(data)
            elif not self.right.data:
                self.right.insert(data)
            elif not self.data:
                self.data = data
                self.counter = counter
                counter = permacounter
            else:
                raise
        elif not counter:                       # When the value of counter hits 0, self.data and self.counter gets set
            if not self.data:
                self.data = data
                self.counter = counter
                counter = permacounter
            else:
                raise

    def viewData(self):
        return self.data
    def viewCounter(self):
        return self.counter

def solution(q, l):
    global permacounter, counter
    permacounter = q
    counter = permacounter
    root = Node()
    i = 1
    while True:                 # Loop that populates the binary tree
        try:
            root.insert(i)
            i += 1
        except:
            break
    listc, listd = [], []
    for obj in gc.get_objects():        # Fill lists with Node objects data, and counter
        if isinstance(obj, Node):
            listc.append(obj.viewData())
            listd.append(obj.viewCounter())
    listc.reverse()
    listd.reverse()
    answer = []
    for each in l:                              # Loop to find the value in the binary tree that is above each integer in the list
        listcIndex = (listc.index(each))
        listcIndexCounter = listd[listcIndex]
        try:
            answerIndex = (listd.index(listcIndexCounter + 1, listcIndex))
            answer.append(listc[answerIndex])
        except:
            answer.append(-1)
    return answer
