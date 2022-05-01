#числа Армстронга на интервале 100 до 10000
for num in range (100, 10000):
	num_sum = 0
	num_ = num
	n = len(str(num))
	while num_:
		num_sum += (num_%10)**n
		num_ //= 10
	if num == num_sum:
		print(num)