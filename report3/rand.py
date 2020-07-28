import random

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # 荷物
Ai = [3, 6, 5, 4, 8, 5, 3, 4, 3, 5, 6, 4, 8, 7, 11, 8, 14, 6, 12, 4]  # 重量
Ci = [7, 12, 9, 7, 13, 8, 4, 5, 3, 10, 7, 5, 6, 14, 5, 9, 6, 12, 5, 9]  # 価格
a = {}  # 評価値
max_Ai = 55  # 最大容量
answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 解変数
weight = 0  # 総重量
price = 0  # 総価格

# ランダムに一つ選び、袋に入れる
rand = random.choice(i)
answer[rand - 1] = 1  # ランダムに選んだ荷物の解変数を１にする
weight += Ai[rand - 1]  # ランダムに選んだ荷物を袋にいれる

# 評価値を計算
for _ in i:
    a[_] = Ci[_ - 1] / Ai[_ - 1]  # 評価値＝価格÷重量

# 評価値の高い荷物を袋に入れていく
for j in range(len(i)):
    max_key = max(a, key=a.get)  # 評価値の最も高い荷物ｉを選ぶ
    if weight + Ai[max_key - 1] < max_Ai and answer[max_key - 1] == 0:  # 荷物ｉを袋に入れたとき、最大容量以下かつ荷物ｉの解変数が０のとき袋にいれる
        weight += Ai[max_key - 1]
        answer[max_key - 1] = 1  # 荷物ｉの解変数を１にする
        price += Ci[max_key - 1]
    del a[max_key]  # 選んだ評価値を辞書から削除する

print(answer)
print("weight =", weight)
print("price =", price)
