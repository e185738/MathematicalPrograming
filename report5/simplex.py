import copy

x1 = []
x2 = []
x3 = [14, 1, 2]
x4 = [8, 1, 1]
x5 = [18, 3, 1]
z = [0, -2, -1]
X_line = [x3, x4, x5, z] #シンプレックスタブローの列の変数を入れる
answer = [x3, x4, x5, 0, 0] #シンプレックスタブローの列の変数xと、変数xの数になるまで０で埋める

#シンプレックスタブローを出力する関数
def print_tb(X):
    for _ in X:
        print(_)
    print("\n")

#PEを探す関数
def PE_selector(X_line, Z):
    z_dict = {}
    #（１）zの行で、負の値で絶対値最大のものを選ぶ
    for i in range(len(Z)):
        if Z[i] < 0:
            z_dict[i] = abs(Z[i])

    line = max(z_dict, key=z_dict.get)

    #（２）選んだ列の正値で定数の列の値を割る
    d = {}
    flag = 0
    for j in X_line:
        if j[line] > 0:
            d[flag] = j[0] / j[line]
        else:
            pass
        flag += 1

    #（３）（２）で得られた値のうちから最小値を選ぶ
    try:
        row = min(d, key=d.get) #PEを持つxの行を選ぶ
    except ValueError:
        print("PEの列の値が全て０または負のため、最適解は存在しない") # PEの列の値が全て０または負の場合は最適解は存在しない
        exit()

    answer.remove(X_line[row])
    answer.insert(line - 1, X_line[row])

    return [line, row] #[Zの列, Xの行]

#PEの行を計算する関数
def line_cal(X, PE_list):
    PE = copy.copy(X[PE_list[1]][PE_list[0]])
    print("PE =", PE)

    for i in range(len(X[PE_list[0]])):
        X[PE_list[1]][i] /= PE

    print("PEの行を計算すると、")
    print_tb(X)  

#新しいシンプレックスタブローを求める関数
def next_tab(X, PE_list):
    #計算の都合上PEの列以外の値から計算する
    flag = 0
    for x in X:
        for num in range(len(x)):
            if flag != PE_list[1] and num != PE_list[0]:
                x[num] = x[num] - x[PE_list[0]] * X[PE_list[1]][num] 
            else:
                pass
        flag += 1
    #飛ばしたPEの列の値を計算する
    flag = 0
    for x in X:
        for num in range(len(x)):
            if flag != PE_list[1] and num == PE_list[0]:
                x[num] = x[num] - x[PE_list[0]] * X[PE_list[1]][num]
            else:
                pass
        flag += 1

    print("次のシンプレクスタブローは、")
    print_tb(X)

print("最初のシンプレックスタブローは、")
print_tb(X_line)

while True:
    if min(z) >= 0: #Zの行が全て０または正ならば、すでに最適解である。
        break
    PE_list = PE_selector(X_line, z)
    line_cal(X_line, PE_list)
    next_tab(X_line, PE_list)

print("解）")  
for _ in range(len(answer)):
    if answer[_] != 0:
        answer[_] = round(answer[_][0])
print(answer)
print("Z = ", round(z[0]))

