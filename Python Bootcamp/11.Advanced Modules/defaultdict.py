from collections import defaultdict

d = {"k1": 1}
print(d["k1"])
# print(d["k2"])  # not defined
d = defaultdict(object)
print(d["one"])

for item in d:
    print(item)

d = defaultdict(lambda: 0)
d["one"]  # default assignment = 0

print(d)

d["two"] = 2
print(d)
