import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    def load(self, path):
        arr = mpimg.imread(path)
        to_print = "Loading image of dimensions {w} x {h}"
        print(to_print.format(w=arr.shape[1], h=arr.shape[0]))
        return arr

    def display(self, array):
        plt.imshow(array)
        plt.show()
