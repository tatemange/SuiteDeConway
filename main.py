

"""
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
"""

class SuiteDeConway:
    def __init__(self, startNumber, limit):
        self._nb = str(startNumber)
        self.limit = limit


    def get(self):
        return self._nb


    def set(self, value):
        self._nb = str(value)
    

    def destructurer(self):
        pass
    
    nb = property(get, set)

suite = SuiteDeConway(1, 10)
a.nb = 101
print(a.nb)