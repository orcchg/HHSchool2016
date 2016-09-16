import math

def fact(x):
	y = 1
	for i in range(1, x + 1):
		y *= i
	return y

def s(n):
	for i in range(1, 31):
		y = fact(i)
		if y % n == 0:
			return i
#	print("larger than 30!")
	return -1

#print(s(860000000))
#print(s(870000000))

def S(M, N):
	sum = 0
	for i in range(M, N + 1):
		print(i)
		r = s(i)
		if r != -1:
			sum += r
	return sum

#print(S(860000000, 870000000))

###############################################################################
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

#print(max(prime_factors(860000000)))
#print(max(prime_factors(fact(43))))

def x(n_factors, f_factors):
	n_factors_c = n_factors[:]
	for i in n_factors_c:
		try:
			f_factors.remove(i)
		except ValueError:
			x = 1
		else:
			n_factors.remove(i)
	return n_factors


def z(n):
	n_factors = prime_factors(n)
	r = max(n_factors)
	n_factors.remove(r)
	#print(n_factors)
	f_factors = []
	for i in range(2, r):
		v = prime_factors(i)
		for i in v:
			f_factors.append(i)
	f_factors.sort()
	#return f_factors
	a = x(n_factors, f_factors)
	if len(a) == 0:
		return r
	else:
		r += 1
		r_factors = prime_factors(r)
		b = x(a, r_factors)
		#print("R:", r, r_factors, b)
		while len(b) > 0:
			r += 1
			r_factors = prime_factors(r)
			b = x(b, r_factors)
			#print("R:", r, r_factors, b)
		return r

def MAGIC(z, a):
	m = a
	n = 0
	for i in range(z, a):
		b = max(prime_factors(i))
		if (b < m):
			m = b
		if (b > n):
			n = b
	return [m, n]

# 860000100: [43, 860000077]
# 860001000: [43, 860000969]
# 860010000: [43, 860009987]
# 860100000: [13, 860099987]
#print(MAGIC(860000000, 860100000))
#print(z(860000001))


###############################################################################
#[5, 172000019]
#[2, 2, 2, 2, 2, 26875003]
#[3, 11, 17, 19, 80683]
#[2, 11701, 36749]
#[7, 122857157]

def solve1(n):
	n_factors = prime_factors(n)
	r = max(n_factors)
	n_factors.remove(r)
	if len(n_factors) == 0:
		return r
	r += 1
	f_factors = prime_factors(r)
	a = x(n_factors, f_factors)
	while len(a) > 0:
		r += 1
		f_factors = prime_factors(r)
		a = x(a, f_factors)
	return r

print(solve1(860000000))

