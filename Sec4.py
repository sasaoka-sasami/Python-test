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