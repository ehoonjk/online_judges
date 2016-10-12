class NestedIterator(object):
    def __init__(self, nestedList):
        self.flattenedList = []
        self.flatten(nestedList)
        self.idx = -1

    def flatten(self, nestedList):
        for val in nestedList:
            if isinstance(val, int):
                self.flattenedList.append(val)
            else:
                if len(val) > 1:
                    self.flatten(val)
                else:
                    self.flattenedList.append(val)

    def next(self):
        self.idx += 1
        return self.flattenedList[self.idx]


    def hasNext(self):
        try:
            if self.flattenedList[self.idx+1]:
                return True
        except IndexError:
            return False