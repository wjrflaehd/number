import random

r = random.randint(1, 100)
while True:
	num = input('Please input number: ')
	num = int(num)
	if num == r:
		print('Success')
		break
	elif num > r:
		print('Too big')
	elif num < r:
		print('Too small')