s = [i.lower() for i in input().split()]
d = {x : s.count(x) for x in s}
for i in d.keys():
    print(i, d[i])