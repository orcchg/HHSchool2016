def solve(n):
	r = 1
	for i in range(3, n + 1, 2):
		s = i**2
		b = i - 1
		v = s * 4 - b * 6
		r += v
	return r

print(solve(3))
print(solve(5))
print(solve(7))
print(solve(1143))

