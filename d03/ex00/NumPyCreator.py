import numpy as np


class NumPyCreator:

    def from_list(self, lst):
        arr = np.array(lst)
        return arr

    def from_tuple(self, tpl):
        arr = np.array(tpl)
        return arr

    def from_iterable(self, itr):
        if type(itr) == range:
            arr = np.array(itr)
        else:
            arr = np.arange(itr)
        return arr

    def from_shape(self, shape, value=0):
        arr = np.ones(shape, dtype=int) * value
        return arr

    def random(self, shape):
        arr = np.random.random(shape)
        return arr

    def identity(self, n):
        arr = np.eye(n, dtype=int)
        return arr
