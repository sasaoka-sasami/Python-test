#セクション4演習：ランダムに話題を提示するさいころを作成する
import random
talk_list = ['名前の由来', '出身地の好きなところ', '最近食べた美味しいもの', '残念に思った話', '好きな本', '好きなゲーム', '好きな食べ物']
num = random.randint(0, 6)
print(talk_list[num])