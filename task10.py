# task10


def calculate_average(marks):
	total = 0
	for key in marks:
		total = total + marks[key]
	average = total / len(marks)
	return average


def display_average(mark):
	print(mark)


def main():
	marks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
	display_average(calculate_average(marks))


if __name__ == '__main__':
	main()