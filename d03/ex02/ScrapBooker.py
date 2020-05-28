import numpy as np


class ScrapBooker:

    def crop(self, array, dimensions, position=(0, 0)):
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            print("Error: the dimensions is larger than shape.")
            return None
        else:
            crop_x = position[1] + dimensions[1]
            crop_y = position[0] + dimensions[0]
            if crop_x > array.shape[1] or crop_y > array.shape[0]:
                print("Error: the dimensions is larger than shape.")
                return None
            return array[position[1]:crop_x, position[0]:crop_y]

    def thin(self, array, n, axis):
        axis = 1 - axis
        if axis == 1 or axis == 0:  # Vertical == 1 Horizontal == 0
            arr = np.delete(array, np.s_[n-1::n], axis)
            return arr
        else:
            print("Error: the axis is not egal to 0 or 1.")
            return None

    def juxtapose(self, array, n, axis):
        axis = 1 - axis
        if axis == 1 or axis == 0:  # Vertical == 1 Horizontal == 0
            arr = np.concatenate([array] * n, axis)
            return arr
        else:
            print("Error: the axis is not egal to 0 or 1.")
            return None
        pass

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions + (1,))
