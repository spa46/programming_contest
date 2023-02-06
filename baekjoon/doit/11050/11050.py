import sys

n, r = map(int, sys.stdin.readline().split())

nFact = 1
nrFact = 1
rFact = 1

# n! / n-r! r!

for i in range(1, n+1):
    nFact *= i

for i in range(1, n-r+1):
    nrFact *= i

for i in range(1, r+1):
    rFact *= i

print(int(nFact/(nrFact*rFact)))










