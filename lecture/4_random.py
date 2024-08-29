"""
他のプログラムを使う
"""

# randomモジュールを使えるようにします。
import random

# 0以上1未満のランダムな小数を作ります。
r1 = random.random()
print(r1)

# 1以上10以下のランダムな整数を作ります。
r2 = random.randint(1, 10)
print(r2)
