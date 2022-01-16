import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, r, c = map(int, input().split())

result = 0

for i in range(N) :
	result += (2**(2*N - 1 - 2*i)) * (r // (2**(N-i-1)))
	result += (2**(2*N - 2 - 2*i)) * (c // (2**(N-i-1)))
	r = r % (2**(N-i-1))
	c = c % (2**(N-i-1))

print(result)