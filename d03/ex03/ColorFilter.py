import numpy as np


class ColorFilter:

	def invert(self, array):
		return (1 - array[...,0:3])

	def to_blue(self, array):
		zeros = np.zeros(array.shape)
		zeros[:, :, 2] = array[:, :, 2]
		zeros[:, :, 3] = array[:, :, 3]
		return zeros

	def to_green(self, array):
		new = np.zeros(array.shape)
		new[:, :, 1] = array[:, :, 1]
		new[:, :, 3] = array[:, :, 3]
		return new

	def to_red(self, array):
		arr = array - self.to_blue(array) - self.to_green(array)
		return arr[...,0:3]

	def celluloid(self, array):
		pass