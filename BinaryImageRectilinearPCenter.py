import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

import imageio
import argparse

def visualization(im_binary, W, res):
	plt.imshow(im_binary)
	
	n = res[0]
	M, N = im_binary.shape

	for i in range(1, n+1):
		row, col = res[i]

		x1 = col-0.5
		y1 = row-0.5
		x2 = min(col + W - 1, N-1)+0.5
		y2 = min(row + W - 1, M-1)+0.5
		plt.plot((x1, x2), (y1, y1), 'r-')
		plt.plot((x1, x2), (y2, y2), 'r-')
		plt.plot((x1, x1), (y1, y2), 'r-')
		plt.plot((x2, x2), (y1, y2), 'r-')

	plt.show()

def solve(Ones, inList, W, maxP):
	if maxP < 1:
		if np.count_nonzero(inList) > 0:
			return [-1]
		else:
			return [0]
	if np.count_nonzero(inList) == 0:
		return [0]

	### Find the bounding box
	row_min = -1
	row_max = -1
	col_min = -1
	col_max = -1
	N = len(Ones)
	for i in range(N):
		### Only consider points that have not been covered yet
		if inList[i] == 0:
			continue

		x, y = Ones[i]
		if row_min == -1 or row_min > x:
			row_min = x
		if row_max == -1 or row_max < x:
			row_max = x
		
		if col_min == -1 or col_min > y:
			col_min = y
		if col_max == -1 or col_max < y:
			col_max = y

	### Always return the co-ordinate of the top-left corner of the squares
	### Base case: maxP = 1.
	if maxP == 1:
		if row_max - row_min + 1 <= W and col_max - col_min + 1 <= W:
			return [1, (row_min, col_min)]
		else:
			return [-1]
	
	### All 4 corners
	tries = []
	## corners = [(row_min, col_min), (row_min, col_max), (row_max, col_min), (row_max, col_max)]
	
	if maxP <= 3:
		tries.append((row_min, col_min))
		if col_max - W + 1 > col_min:
			tries.append((row_min, col_max - W + 1))
		if row_max - W + 1 > row_min:
			tries.append((row_max - W + 1, col_min))
		if col_max - W + 1 > col_min and row_max - W + 1 > row_min:
			tries.append((row_max - W + 1, col_max - W + 1))
	else:
		for r in range(row_min, max(row_min, row_max - W + 1) + 1):
			tries.append((r, col_min))

	save = list(inList)
	res_n = -1
	res = []
	sub_res = []
	sub_res_idx = -1

	idx = 0
	for r, c in tries:
		### Remove the points that will be covered by this square
		# print("r, c = {}, {}".format(r, c))

		for i in range(N):
			if inList[i] == 0:
				continue

			x, y = Ones[i]
			if x >= r and x - r + 1 <= W and y >= c and y - c + 1 <= W:
				inList[i] = 0

		### Solve next
		tmp = solve(Ones, inList, W, maxP - 1)
		if tmp[0] != -1:
			if res_n == -1 or res_n > tmp[0] + 1:
				res_n = tmp[0] + 1
				sub_res = tmp
				sub_res_idx = idx

		idx += 1
		### Recover the inList
		inList = list(save)

		# print("after idx = {}, res_n is {}".format(idx-1, res_n))

	if res_n == -1:
		return [-1]
	else:
		res.append(res_n)
		res.append(tries[sub_res_idx])

		if res_n > 1:
			res.extend(sub_res[1:])
		
		return res


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Read image and generate covering squares")
	parser.add_argument("-i", "--image", type=str, nargs='?', help="image file")
	parser.add_argument("-t", "--threshold", type=float, nargs='?', help="threshold in percent of the maximum intensity")
	parser.add_argument("-m", "--maxP", type=int, nargs='?', help="maximum number of squares")
	parser.add_argument("-w", "--W", type=int, nargs='?', help="square size")

	### Reading arguments
	args = parser.parse_args()

	if args.image is None:
		raise Exception("The image file is unspecified")

	if args.threshold is not None:
		threshold = args.threshold
	else:
		threshold = 25

	if args.maxP is not None:
		maxP = args.maxP
	else:
		maxP = 4

	if args.W is not None:
		W = args.W
	else:
		W = 24

	### Reading the original image
	im_original = imageio.imread(args.image)

	print(im_original.shape, np.min(im_original), np.max(im_original))

	### Thresholding to obtain the binary image

	intensity_threshold = np.max(im_original) * threshold / 100.0

	im_binary = np.where(im_original >= intensity_threshold, 1, 0)
	print(im_binary.shape, np.min(im_binary), np.max(im_binary))

	### im_binary = np.random.randint(0, 2, im_binary.shape) ### Test on random binary images

	### Finding the covering squares or Outputing "Infeasible"

	M, N = im_binary.shape

	plt.imshow(im_binary)
	plt.show()

	Ones = []
	for i in range(M):
		for j in range(N):
			if im_binary[i][j] == 1:
				Ones.append((i,j))

	res = solve(Ones, [1] * len(Ones), W, maxP)
	if res[0] == -1:
		print("Cannot cover all bright pixels with {} squares".format(maxP))
	else:
		print("Number of squares needed = {}".format(res[0]))
		print("Positions of the squares:")
		for i in range(1, res[0]+1):
			print("(row, col) = {}".format(res[i]))	

		print("Visualization:")
		visualization(im_binary, W, res)

