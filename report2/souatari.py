# coding: utf-8
# [荷物, 容量, 価格]
goods = [[1, 3, 7], [2, 6, 12], [3, 5, 9], [4, 4, 7], [5, 8, 13], [6, 5, 8], [7, 3, 4], [8, 4, 5]]

import itertools

list = []
answer = []
max_price = 0
max_capa = 25

#荷物の組み合わせをlistに格納する
for i, _ in enumerate(goods, 1):
    for i in itertools.combinations(goods, r=i):
        list.append(i)

    #解を見つける
    for j in list:
        capa_num = 0
        price_num = 0
        for k in j:
            capa_num += k[1]
            price_num += k[2]
        if capa_num == max_capa and price_num > max_price:
            max_price = price_num
            answer = j

print("荷物の組み合わせ =", answer)
print("Price =", max_price)
print("Capacity =", max_capa)
