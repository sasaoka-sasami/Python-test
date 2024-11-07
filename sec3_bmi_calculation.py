#sec3演習：キーボードから値を入力してBMIを求める

#キーボードで身長と体重を入力
height = float(input('身長を入力[m]：'))
weight = float(input('体重を入力[kg]：'))

#BMIの計算
bmi = weight / (height * height)

#出力
print('BMI: '+ str(bmi))