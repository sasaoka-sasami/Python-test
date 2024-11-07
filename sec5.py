#条件分岐の使い方
score = int(input('点数を入力：'))
# コロンを忘れやすいから注意
if score >= 80:
    print('good!')
elif score >= 50:
    print('OK')
else:
    print('NG')

# スコアリストに100があったら出力
scores = [1, 2, 3, 100]
if 100 in scores:
    print('100があります')