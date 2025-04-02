

"""
EXAMPLE:
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

    def destructurer(self, string):
        count = 1
        newString = []
        i = 0
        while i < (len(string)-1):
            if(string[i] == string[i+1]):
                count += 1
            else:
                newString.extend([str(count) + string[i]])
                count = 1
            i += 1 
        newString.extend([str(count) + string[i]])
        return "".join(newString)

    def back(self, string):
        newString = []
        for i in range(0, len(string), 2):
            for j in range(int(string[i])):
                newString.extend([string[i+1]])
        
        return "".join(newString)
    
    def view(self):
        print(self._nb)
        new = self.destructurer(self._nb)
        print(new)
        for i in range(self.limit-1):
            new = self.destructurer(new)
            print(new)

        self.end = new

    def viewBack(self):
        new = self.back(self.end)
        print(new)
        for i in range(self.limit-1):
            new = self.back(new)
            print(new)

    nb = property(get, set)



suite = SuiteDeConway(1, 14)
suite.view()
suite.viewBack()
