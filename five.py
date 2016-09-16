# 2 < a < 107 & 2 < b < 116

def solve(abot, atop, bbot, btop):
	t = 0
	s = set()
	for a in range(abot + 1, atop):
		for b in range(bbot + 1, btop):
			t += 1
			s.add(a**b)
	return len(s)

print(solve(1, 6, 1, 6))
print(solve(2, 107, 2, 116))

