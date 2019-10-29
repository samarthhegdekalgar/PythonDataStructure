def merge(left, right):
	new_arr = []
	l_index, r_index = 0,0
	while l_index < len(left) and r_index < len(right):
		if left[l_index] <= right[r_index]:
			new_arr.append(left[l_index])
			l_index += 1
		else:
			new_arr.append(right[r_index])
			r_index += 1
	new_arr += left[l_index:]
	new_arr += right[r_index:]
	return new_arr


def merge_sort(arr):
	if len(arr) <=1:
		return arr

	mid = len(arr)//2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left, right)


arr = [10, 4, 5, 2, 100, 13]

print(merge_sort(arr))