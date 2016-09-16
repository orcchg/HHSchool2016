def isCorrect(r, q, v, w, x):
	a = 100*r + 10*q + r
	b = 100*v + 10*v + w
	c = 100*w + 10*v + x
	d = a + b == c
	return d

#print(isCorrect(1, 0, 2, 3, 4))
#print(isCorrect(1, 0, 2, 3, 5))

def solve():
	answer = 0
	total = 0
	for r in range(1, 10):
		for v in range(1, 10):
			if v == r:
				continue
			for w in range(1, 10):
				if w == r or w == v:
					continue
				for q in range(0, 10):
					if q == r or q == v or q == w:
						continue
					for x in range(0, 10):
						if x == q or x == r or x == v or x == w:
							continue
						total += 1
						if isCorrect(r, q, v, w, x):
							print(r,q,r,'+',v,v,w,'=',w,v,x)
							answer += 1
	return [answer, total]

print(solve())

