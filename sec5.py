#条件分岐の使い方
score = int(input('点数を入力：'))
# コロンを忘れやすいから注意
if score >= 80:
    print('good!')
elif score >= 50:
    print('OK')
else:
    print('NG')