

def fib():
	fib = [0, 1, 1]

	for x in range(3,20000000000000):
		xFib = fib[x-1] + fib[x-2]
		print(len(str(xFib)))
		fib.append(xFib)
		
		if(len(str(xFib)) >= 1000):
			print("Sucess! " + str(x))
			return 0	


fib()
