import matplotlib.pyplot as plt
import numpy as np
import imageio
from skimage.color import rgb2gray
import cv2

trace = dict()

def solve(binary_image, image_height, image_width, window_size, current_column, current_row):
	# if current_column == 5:
	#  	print("solving at: {}, {}".format(current_column, current_row))
	
	if current_column >= image_width:
		trace[(current_column, current_row)] = (-1, -1, 0)
		
		return 0
	if current_row >= image_height:
		ret = solve(binary_image, image_height, image_width, window_size, current_column + 1, 0)
		trace[(current_column, current_row)] = trace[(current_column + 1, 0)]
		
		return ret
	# if (current_column, current_row) in trace:
	#  	return trace[(current_column, current_row)][2]

	ret = image_height * image_width # abitrary large number
	ret_top_left = -1 # the row of the top left position of the window

	has_1 = False
	for row in range(current_row, image_height):
		if binary_image[row][current_column] == 1:
			has_1 = True
			for top_left in range(row - window_size + 1, row+1):
				if top_left >= 0 and top_left < image_height:
					right_border = current_column + window_size
					if right_border > image_width:
						right_border = image_width
					n1 = 0
					for j in range(current_column, right_border):
						n1 += binary_image[top_left][j]
					if n1 == 0:
						continue
					### Putting a window here
					# print("current_column = {}, found 1 at row = {}, putting a top_left at {}".format(current_column, row, top_left))
					### Step 1: mark every 1 in this window to 0
					### Step 2: solve the corresponding sub-problem
					### Step 3: recover the 1s after that
					ret_tmp = 0
					list_one = list()

					### Step 1
					for i in range(top_left, top_left + window_size):
						for j in range(current_column, current_column + window_size):
							if i >= 0 and i < image_height and j >= 0 and j < image_width and binary_image[i][j] == 1:
								list_one.append((i,j))
								binary_image[i][j] = 0
					### Step 2
					ret_tmp = 1 + solve(binary_image, image_height, image_width, window_size, current_column, top_left + window_size)
					if ret_tmp <= ret:
						ret = ret_tmp
						ret_top_left = top_left

					### Step 3
					for (i, j) in list_one:
					 	binary_image[i][j] = 1

			break

	if ret_top_left == -1:
		if has_1 is True:
			ret = -np.inf
			print("SOMETHING WRONG! current_column = {}, current_row = {}".format(current_column, current_row))
		else:
			assert(has_1 is False)
			# print("solving at: {}, {}, moving to next column".format(current_column, current_row))
			ret = solve(binary_image, image_height, image_width, window_size, current_column + 1, 0)
			trace[(current_column, current_row)] = trace[(current_column + 1, 0)]
	else:
		# print("solving at: {}, {}, moved to row {}, result here = {}".format(current_column, current_row, ret_top_left + window_size, ret))
		trace[(current_column, current_row)] = (ret_top_left, current_column, ret)

	return ret


window_size = 24
threshold = 50

im_original = imageio.imread('MultiGradient2.png')


print(im_original.shape, np.min(im_original), np.max(im_original))

# print(im_original)

im_binary = np.where(im_original > threshold, 1, 0)

# SIZE = 50
# im_binary = np.random.randint(low=0, high=2, size=(SIZE, SIZE))
# print(im_binary.dtype, im_binary.shape, np.min(im_binary), np.max(im_binary))

H, W = im_binary.shape

plt.imshow(im_binary)
plt.show()

print(im_binary.shape, np.min(im_binary), np.max(im_binary))
save_im_binary = im_binary.copy()

# for i in range(W):
# 	for j in range(H):
# 		if im_binary[j][i] == 1:
# 			print("(col, row) = ({}, {})".format(i, j))

# res_top_left = list()
result = solve(im_binary, H, W, window_size, 0, 0)
print("result = {}".format(result))

### sanity check
assert(np.array_equal(save_im_binary, im_binary))
top_left = trace[(0, 0)]

plt.imshow(save_im_binary)

for it in range(result):
	row, col, ret = top_left
	print("top_left of window is row = {}, col = {}".format(row, col))
	for r in range(row, row + window_size):
		for c in range(col, col + window_size):
			if r >= 0 and r < H and c >= 0 and c < W:
				im_binary[r][c] = 0

	x1 = col-0.5
	y1 = row-0.5
	x2 = min(col + window_size - 1, W-1)+0.5
	y2 = min(row + window_size - 1, H-1)+0.5
	plt.plot((x1, x2), (y1, y1), 'r-')
	plt.plot((x1, x2), (y2, y2), 'r-')
	plt.plot((x1, x1), (y1, y2), 'r-')
	plt.plot((x2, x2), (y1, y2), 'r-')

	next_col = col
 	next_row = row + window_size
 	if it < result - 1:
 		top_left = trace[(next_col, next_row)]

print("count nonzero = {}".format(np.count_nonzero(im_binary)))
plt.show()

# print("res_top_left = {}".format(res_top_left))

