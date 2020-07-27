# coding: utf-8
# [荷物, 容量, 価格]
goods = [[1, 3, 7], [2, 6, 12], [3, 5, 9], [4, 4, 7], [5, 8, 13], [6, 5, 8], [7, 3, 4], [8, 4, 5],[9 ,3 ,3] ,[10 ,5 ,10] ,[11 ,6 ,7] ,[12 ,4 ,5] ,[13 ,8 ,6] ,[14 ,7 ,14] ,[15 ,11 ,5] ,[16 ,8 ,9] ,[17 ,14 ,6] ,[18,6,12],[19,12,5],[20,4,9]]

import itertools

list = []
answer = []
max_price = 0
max_capa = 55

#荷物の組み合わせをlistに格納する
for i, _ in enumerate(goods, 1):
    for i in itertools.combinations(goods, r=i):
        list.append(i)

#容量が丁度限界に達する組み合わせをlist2に格納する
    for j in list:
        capa_num = 0
        price_num = 0
        for k in j:
            capa_num += k[1]
            price_num += k[2]
        if capa_num == max_capa and price_num > max_price:
            max_price = price_num
            answer = j
print(len(list))
print("荷物の組み合わせ =", answer)
print("Price =", max_price)
print("Capacity =", max_capa)

#A2価格が最大のものを格納する
"""
A = 0
for i in list2:
    max = 0
    for g in i:
        max += g[2]
    if A < max:
        A = max
        A2 = []
        A2 = i"""

# 価格と容量を求める
"""
Price = 0
Capacity = 0
for i in A2:
    Price += i[2]
    Capacity += i[1]
print("Price =", Price)
print("Capacity =", Capacity)"""
