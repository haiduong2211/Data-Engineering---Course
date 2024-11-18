n = input()
a = set(n.split())
total = 0
for v in a:
    total += float(v)
print(round(total/len(a),2))
