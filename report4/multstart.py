import random
import copy

# 英語＝１、数学＝２、物理＝３、化学＝４
subject = [1, 2, 3, 4]
A = [6, 1, 9, 3]
B = [2, 5, 7, 8]
C = [6, 3, 5, 4]
D = [3, 5, 2, 1]
fx = 0  # 初期解の目的関数
fx_list = []  # 目的関数のリスト
answer_list = [] #暫定解候補
best_fx = 0 #最小の目的関数
P = 5 #初期解の数


# 初期解をランダムに生成
# s=[A,B,C,D]
s = []
for _ in range(int(P)):
    s.append(random.sample(subject, len(subject)))

# 全ての初期解に局所探索法を適用
# 隣り合う要素を入れ替えることを摂動とする
for i in s:
    frag = 0
    list = []  # 近傍解の目的関数のリスト
    N = []  # 近傍解
    fx = A[i[0] - 1] + B[i[1] - 1] + C[i[2] - 1] + D[i[3] - 1]
    for _ in range(len(subject) - 1):
        x = copy.copy(i)
        x[frag], x[frag + 1] = x[frag + 1], x[frag] #隣り合う要素を入れ替える
        N.append(x) #入れ替えたものを近傍解リストに入れる
        fx1 = A[x[0] - 1] + B[x[1] - 1] + C[x[2] - 1] + D[x[3] - 1] #近傍解の目的変数
        list.append(fx1) #近傍解の目的変数をリストに入れる
        frag += 1
    if min(list) < fx: 
        fx = min(list)
        fx_list.append(fx)
        answer_list.append(N[list.index(min(list))])

# 目的関数が最小の解を探す
best_fx = min(fx_list)
answer = answer_list[fx_list.index(min(fx_list))]

print("最良解＝", answer)
print("総作業時間＝", best_fx)