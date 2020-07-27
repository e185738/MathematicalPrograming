i = [1, 2, 3, 4, 5, 6, 7, 8]
Ai = [3, 6, 5, 4, 8, 5, 3, 4]
Ci = [7, 12, 9, 7, 13, 8, 4, 5]
a = {}
max_Ai = 25
answer = [1, 1, 1, 1, 1, 1, 1, 1]
A = sum(Ai)

for _ in i:
    a[_] = Ci[_ - 1] / Ai[_ - 1]

"""
max_key=max(a, key=a.get)
max_value=max(a.values())
A+=max_value
print(A)"""

for j in range(len(i)):
    min_key = min(a, key=a.get)
    if A - Ai[min_key - 1] > max_Ai:
        A -= Ai[min_key - 1]
        answer[min_key - 1] = 0
    del a[min_key]

print(answer)
print(A)
