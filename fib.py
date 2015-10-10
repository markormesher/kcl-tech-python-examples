# prints the nth fibonacci number

def fib(n):
	# check that the fibonacci number being asked for is valid
	assert n >= 0

	# the first 2 fibonacci numbers
	a = 0
	b = 1

	# if we are asked for either of the first 2 fibonacci numbers, return them since we know what they are
	if n == 0:
		return a
	elif n == 1:
		return b

	# otherwise we need to work out what the nth fibonacci number is
	for i in range(1, n):
		fibSum = a + b
		a = b
		b = fibSum

	# and then return it
	return b

print(fib(7))
