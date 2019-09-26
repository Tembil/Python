import cmath 

def solve(a, b, c):
	d = b ** 2 - 4 * a * c
	x1 = (-b - cmath.sqrt(d))/(2 * a)
	x2 = (-b + cmath.sqrt(d))/(2 * a)
	return x1, x2