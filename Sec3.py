#hello, worldを出力
print("hello, World")
#Sec2演習
print('Hello, Python!')

#Sec3
#数値リテラルの出力
print(1_000_000)
#べき乗=2^3
print(2 ** 3)
#文字列出力は日本語もok
print('こんにちは')
#エスケープシーケンスがあれば'も出力できる
print('I\'mfime.')
#文字列を操作
print('1'+'1')#=11
print(len('hello'))#=5

#変数を使う
#送料こみ代金を出力
delivary_fee = 500
print(1000 + delivary_fee)#=1500
delivary_fee = 250
print(1000 + delivary_fee)#=1250

#キーボードから直接値を入力
name = input('please enter your name.')
print('Hello' + name + 'san.')

#データ型を変換
price = int(input('価格を入力'))
print(price)
count = int(input('人数を入力'))
print(count)
# print(type(price))
# print(type(count))
print(price/count)