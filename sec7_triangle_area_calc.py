# セクション7 演習：3角形の面積を求めて返す
# 講座からの変更点：底辺の長さ、高さをユーザー入力で設定する方法に変更, 表示を小数点2位まで表示に変更

# 三角形の面積を計算する
def calc_tri_area(bottom, height):
    area = (bottom * height) / 2.0
    return area

bottom = float(input('底辺を入力[cm]:'))
height = float(input('高さを入力[cm]:'))
print(f'三角形の面積は{calc_tri_area(bottom, height):.2f}cm^2')