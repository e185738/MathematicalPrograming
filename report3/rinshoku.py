i = [1, 2, 3, 4, 5, 6, 7, 8]  # 荷物
Ai = [3, 6, 5, 4, 8, 5, 3, 4]  # 容量
Ci = [7, 12, 9, 7, 13, 8, 4, 5]  # 価格
a = {}  # 評価値
max_Ai = 25  # 最大容量
answer = [0, 0, 0, 0, 0, 0, 0, 0]  # 解変数
weight = 0  # 総重量
price = 0  # 総価格

# 評価値を計算
for _ in i:
    a[_] = Ci[_ - 1] / Ai[_ - 1]  # 評価値＝価格÷重量

# 評価値の高い荷物を袋に入れていく
for j in range(len(i)):
    max_key = max(a, key=a.get)  # 評価値の最も高い荷物ｉを選ぶ
    if weight + Ai[max_key - 1] < max_Ai:  # 荷物ｉを袋に入れたとき、最大容量以下なら袋に入れる
        weight += Ai[max_key - 1]
        answer[max_key - 1] = 1  # 荷物ｉの解変数を１にする
        price += Ci[max_key - 1]
    del a[max_key]  # 選んだ評価値を辞書から削除する

print(answer)
print("weight =", weight)
print("price =", price)
