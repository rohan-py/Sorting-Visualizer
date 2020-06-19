from matplotlib import pyplot as plt
import sorts
import random
from matplotlib import animation
import time


while True:
	plt.style.use('grayscale')


	N = int(input('Enter number of integers: '))
	method = input('''Enter sorting method:
(b)ubble sort
(i)nsertion sort
(m)erge sort
(q)uick sort
(s)election sort\n''')

	A = [random.randint(1, N) for i in range(N)]
	states = []

	if method == 'b':
		title = 'Bubble Sort'
		generator = sorts.bubblesort(A)
	elif method == 'i':
		title = 'Insertion Sort'
		generator = sorts.insertionsort(A)
	elif method == 'm':
		title = 'Merge Sort'
		generator = sorts.mergesort(A, 0, len(A)-1)
	elif method == 'q':
		title = 'Quick Sort'
		generator = sorts.quicksort(A, 0, len(A)-1)
	else:
		title = 'Selection Sort'
		generator = sorts.selectionsort(A)


	#iterator = [i for i in generator]


	



	fig, ax = plt.subplots()
	ax.set_title(title)

	bar_rects = ax.bar(range(len(A)), A, align='edge')

	ax.set_xlim(0, N)
	ax.set_ylim(0, int(1.07 * N))

	text = ax.text(.02, 0.95, '', transform=ax.transAxes)

	iteration = [0]

	

	def update_fig(A, rects, iteration):
		for rect, val in zip(rects, A):
			rect.set_height(val)
		iteration[0] += 1
		text.set_text('# of operations: {}'.format(iteration[0]))

	anim = animation.FuncAnimation(fig, func=update_fig,
		fargs=(bar_rects, iteration), frames=generator, interval=1, repeat=False)

	plt.show()

	
	if input('Want to exit(y/n)? ') == 'y':
		break
	print()
