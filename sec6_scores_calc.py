# セクション6演習：テストの点数の合計値と平均値を求める
scores = [100, 90, 80, 70, 60]
sum = 0

# 合計値の算出
for i in scores:
    sum += i

# 平均値の算出
average = sum / len(scores)

print(f'合計値：{sum}, 平均値：{average}')