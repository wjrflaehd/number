import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('Please input number: ')
	num = int(num)
	if num == r:
		print('Success')
		print('This is the', count, 'time')
		break
	elif num > r:
		print('Too big')
	elif num < r:
		print('Too small')
	print('This is the', count, 'time')