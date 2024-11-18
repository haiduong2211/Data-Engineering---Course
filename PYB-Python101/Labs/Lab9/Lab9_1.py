res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)


def evenNum(res):
    evenlst = []
    for v in res:
        if v % 2 == 0:
            evenlst.append(v)
    print(evenlst)

evenNum(res)
