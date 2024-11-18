n = input().split()
s = set(n)

for i in range(len(n)):
    s.add(n[i])

print(len(s))
