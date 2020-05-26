class Vector:

    def __init__(self, values):
        assert isinstance(values, list) or isinstance(values, int)\
            or isinstance(values, tuple),\
            "The values is not list, int or tuple."
        self.values = list()
        if type(values) == list:
            for val in values:
                assert isinstance(val, float),\
                    "The list doesn't just contain floats."
            self.values = values
        elif type(values) == int:
            for i in range(values):
                self.values.append(float(i))
        elif type(values) == tuple:
            assert len(values) == 2, "The tuples doesn't contain 2 values."
            for i in range(values[0], values[1]):
                self.values.append(float(i))
        self.size = len(self.values)

    def __str__(self):
        txt = "(Vector {vals})".format(vals=self.values)
        return txt

    def __repr__(self):
        txt = "<vector.Vector at {mem}>".format(mem=hex(id(self)))
        return txt

    def __radd__(self, other):
        return self + other

    def __add__(self, other):
        assert isinstance(other, int) or isinstance(other, float)\
            or isinstance(other, Vector),\
            "Other is not a int or a float or a Vector."
        if type(other) == int or type(other) == float:
            newList = list()
            for value in self.values:
                newList.append(value + other)
        elif type(other) == Vector:
            assert self.size == other.size, "Other size it's different."
            newList = list()
            i = 0
            while i < self.size:
                newList.append(self.values[i] + other.values[i])
                i += 1
        return(Vector(newList))

    def __rsub__(self, other):
        assert isinstance(other, Vector), "Other is not a Vector."
        newList = list()
        i = 0
        while i < self.size:
            newList.append(other.values[i] - self.values[i])
            i += 1
        return(Vector(newList))

    def __sub__(self, other):
        assert isinstance(other, int) or isinstance(other, float)\
            or isinstance(other, Vector),\
            "Other is not a int or a float or a Vector."
        if type(other) == int or type(other) == float:
            newList = list()
            for value in self.values:
                newList.append(value - other)
        elif type(other) == Vector:
            newList = list()
            i = 0
            while i < self.size:
                newList.append(self.values[i] - other.values[i])
                i += 1
        return(Vector(newList))

    def __truediv__(self, other):
        assert isinstance(other, int) or isinstance(other, float)\
            or isinstance(other, Vector),\
            "Other is not a int or a float or a Vector."
        if type(other) == int or type(other) == float:
            newList = list()
            for value in self.values:
                newList.append(value / other)
        elif type(other) == Vector:
            newList = list()
            i = 0
            while i < self.size:
                if other.values[i] != 0:
                    newList.append(self.values[i] / other.values[i])
                else:
                    print('Err: div by 0!')
                    return None
                i += 1
        return(Vector(newList))

    def __rtruediv__(self, other):
        assert isinstance(other, Vector), "Other is not a Vector."
        newList = list()
        i = 0
        while i < self.size:
            if other.values[i] != 0:
                newList.append(other.values[i] / self.values[i])
            else:
                print('Err: div by 0!')
                return None
            i += 1
        return(Vector(newList))

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        assert isinstance(other, int) or isinstance(other, float)\
            or isinstance(other, Vector),\
            "Other is not a int or a float or a Vector."
        if type(other) == int or type(other) == float:
            newList = list()
            for value in self.values:
                newList.append(value * other)
        elif type(other) == Vector:
            assert self.size == other.size, "Other size it's different."
            newList = list()
            i = 0
            while i < self.size:
                newList.append(self.values[i] * other.values[i])
                i += 1
        return(Vector(newList))
