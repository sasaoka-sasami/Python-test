#リストの基本的な使い方
scores = [90, 80, 100]
print(scores)

members = ['sasaki', 'tanaka', 'oohashi']
print(members)

#sasakiと80を出力
print(members[0])
print(scores[1])

#長さを求めるときはlen()
print(len(scores))
#要素の合計はsum()
print(sum(scores))
#スライス[以上:未満]
slice_samples = [1, 2, 3, 4, 5]
print(slice_samples[1:3])

#リストの操作
scores = [1, 2, 3, 4, 5]
# 要素の追加
scores.append(6)
print(scores)
#指定した要素を削除
scores.remove(6)
# 末尾の要素を削除
scores.pop()
print(scores)
# インデックス指定削除
scores.pop(2)
print(scores)
# 全ての要素削除
scores.clear
print(scores)

#おみくじプログラム
#実行するたびにランダムに大凶、凶、末吉、吉、小吉、中吉、大吉を表示
import random
omikuji_list = ['大凶', '凶', '末吉', '吉', '小吉', '中吉', '大吉']
num = random.randint(0, 6)
print(omikuji_list[num])