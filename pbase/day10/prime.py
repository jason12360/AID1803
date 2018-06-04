# 1.写一个函数 isprime（x），如果x是素数，返回True，否则，返回False

# 	2.写一个函数prime_m2n(m,n),返回从m开始，到n结束范围内的质数，返回这些质数的列表，并在主程序中打印
# 	如：
# 		L= prime(5,10)
# 		# [5,7]

# 	3.写一个函数primes（n），返回指定范围内的全部素数的列表，并在主程序中打印这些质数
# 		L = primes(100)
# 		# [2,3,5,7,...,97]

def isprime(x):
	for i in range(2,x):
		if x % i == 0:
			break
	else:
		return True
	return False

def prime_m2n(m,n):
	result = []
	for i in range(m,n+1):
		if isprime(i):
			result.append(i)
	return result

def primes(n):
	return prime_m2n(2,n)

print(primes(100))