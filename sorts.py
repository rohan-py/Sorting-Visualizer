#Implementation of popular sorting algorithms as a generator.

def bubblesort(A):
	'''In-place bubble sort.'''
	swapped = True
	for i in range(len(A)):
		if not swapped:
			break
		swapped = False
		for j in range(len(A)-1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				swapped = True
				yield A



def insertionsort(A):
	'''In-place insertion sort.'''
	for i in range(1, len(A)):
		j = i
		key = A[i]
		while j > 0 and A[j-1] > key:
			A[j-1], A[j] = A[j], A[j-1]
			j -= 1
			yield A



def selectionsort(A):
	'''In-place selection sort'''
	for i in range(len(A)-1):
		min = A[i]
		min_index = i
		for j in range(i+1, len(A)):
			if A[j] < min:
				min = A[j]
				min_index = j
				yield A
		A[i], A[min_index] = A[min_index], A[i]
		yield A



def quicksort(A, start, end):
	'''In-place quicksort.'''
	if start >= end:
		return
	
	pivot = A[end]
	p_index = start

	for i in range(start, end):
		if A[i] < pivot:
			A[i], A[p_index] = A[p_index], A[i]
			p_index += 1
		yield A
	A[end], A[p_index] = A[p_index], A[end]
	yield A

	yield from quicksort(A, start, p_index - 1)
	yield from quicksort(A, p_index + 1, end)



def mergesort(A, start, end):
	if end <= start:
		return

	mid = (start + end) // 2
	yield from mergesort(A, start, mid)
	yield from mergesort(A, mid + 1, end)
	yield from merge(A, start, mid, end)

	yield A


def merge(A, start, mid, end):
	merged = []
	leftIdx = start
	rightIdx = mid + 1

	while leftIdx <= mid and rightIdx <= end:
		if A[leftIdx] < A[rightIdx]:
			merged.append(A[leftIdx])
			leftIdx += 1
		else:
			merged.append(A[rightIdx])
			rightIdx += 1

	while leftIdx <= mid:
		merged.append(A[leftIdx])
		leftIdx += 1

	while  rightIdx <= end:
		merged.append(A[rightIdx])
		rightIdx += 1

	for i, val in enumerate(merged):
		A[start + i] = val
		yield A
