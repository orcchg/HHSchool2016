def is_prime(b):
    x = 0.0
    a = 0
    while x<b:
        x=x+1
        #this will check for divisors. 
        if (b/x)-int(b/x) == 0.0:
            a=a+1
    if a==2:
        return True
    else:
        return False

from math import sqrt, ceil

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n/2) if sieve[i]]

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in range(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n/3-correction) if sieve[i]]

def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]

def sieveOfAtkin(end):
    """sieveOfAtkin(end): return a list of all the prime numbers <end
    using the Sieve of Atkin."""
    # Code by Steve Krenzel, <Sgk284@gmail.com>, improved
    # Code: https://web.archive.org/web/20080324064651/http://krenzel.info/?p=83
    # Info: http://en.wikipedia.org/wiki/Sieve_of_Atkin
    assert end > 0
    lng = ((end-1) // 2)
    sieve = [False] * (lng + 1)
    x_max, x2, xd = int(sqrt((end-1)/4.0)), 0, 4
    for xd in range(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d
    x_max, x2, xd = int(sqrt((end-1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not(n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d
    x_max, y_min, x2, xd = int((2 + sqrt(4-8*(1-end)))/4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end: y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x*x + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d
    primes = [2, 3]
    if end <= 3:
        return primes[:max(0,end-2)]
    for n in range(5 >> 1, (int(sqrt(end))+1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, end, 2 * aux):
                sieve[k >> 1] = False
    s  = int(sqrt(end)) + 1
    if s  % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]])
    return primes

#############################################################
from bisect import bisect_left, bisect_right, bisect
from joblib import Parallel, delayed
import multiprocessing

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def find_le(a, x, lo=0, hi=None):
	hi = hi if hi is not None else len(a)
	pos = bisect_left(a,x,lo,hi)
	#print(pos)
	if pos == len(a):
		return pos - 1
	if a[pos] == x:
		return pos
	return pos - 1

N = 11891
sieve = sieveOfAtkin(N + 1)
#print("LEN:",len(sieve))

#def P(n, k):
#	if n > N or k > N or k >= n:
#		return 0
#	table = sieveOfAtkin(n + 1)
#	if k == 1:
#		if table[-1] == n:
#			return 1
#		else:
#			return 0
	########################
#	for i in reversed(table):
#		q = n - i
#		if P(q, k - 1) > 0:
#			return 1
#	return 0


def Po(n, k):
	#print(n,k)
	if k == n // 2:
		return 1
	if n == 1 or n > N or k > N or k >= n:
		return 0
	if k == 1 and n < 4:
		return 1
	pos = find_le(sieve, n)
	if k == 1:
		if sieve[pos] == n:
			return 1
		else:
			return 0
	########################
	for c in range(0, pos + 1):
		i = sieve[pos - c]
		q = n - i
		#print("NEXT",c,i,"[",n,k,"]")
		if Po(q, k - 1) > 0:
			#print("RET:",n,k)
			return 1
	return 0

def process(i):
	s = 0
	j = i // 2
	for k in range(1, j):
		s += Po(i, k)
	return s + 1

def solve(n):
	s = 0
	num_cores = multiprocessing.cpu_count()
	#print("CORES:",num_cores)
	res = Parallel(n_jobs=num_cores)(delayed(process)(i) for i in range(1, n + 1))
	#print(res)
	#for i in range(1, n + 1):
	#	s += process(i)
	return sum(res) - 1


#print(Po(11887, 1))
#print(Po(11891, 25))

print(solve(2))
print(solve(10))
print(solve(20))
print(solve(30))
print(solve(40))
print(solve(50))
#print(solve(60))
#print(solve(70))
#print(solve(80))
#print(solve(90))
#print(solve(100))

#print("#####")
#ll = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#print(bisect_left(ll, 2))
#print(bisect_left(ll, 7))
#print(bisect_left(ll, 19))
#print(bisect_left(ll, 89))
#print(bisect_left(ll, 97))
#print(find_le(ll, 53))
#print(find_le(ll, 55))
#print(find_le(ll, 59))

