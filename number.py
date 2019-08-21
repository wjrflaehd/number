import random
start = input('Please enter start random number: ')
end = input('Please enter end random number: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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